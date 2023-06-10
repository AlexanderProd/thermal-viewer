import cv2
from flirpy.camera.boson import Boson
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt6.QtCore import QSettings

from ui.colormap_selector import ColormapSelector
from ui.aspect_ratio_label import AspectRatioLabel
from utils import apply_colormap, get_file_save_path


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.cap = cv2.VideoCapture(0)
        self.boson = Boson()
        self.colormap = None

        # Create a QTimer to update the video feed
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.recording = False
        self.video_writer = None

        self.settings = QSettings(
            "./settings.ini",
            QSettings.Format.IniFormat,
        )
        self.output_directory = self.settings.value("OutputDirectory", type=str)

    def init_ui(self):
        self.showFullScreen()
        self.setGeometry(0, 10, 640, 512)
        self.setWindowTitle("Thermal Viewer")

        # Create a vertical layout for the toolbar and label
        vertical_layout = QHBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        # Create a toolbar widget and add buttons to it
        toolbar_widget = QWidget()
        toolbar_layout = QVBoxLayout(toolbar_widget)
        toolbar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        screenshot_button = QPushButton("Take Screenshot")
        screenshot_button.clicked.connect(self.take_screenshot)

        recording_button = QPushButton("Start/Stop Recording")
        recording_button.clicked.connect(self.toggle_recording)

        colormap_selector = ColormapSelector(self)

        output_directory_button = QPushButton("Select Output Directory")
        output_directory_button.clicked.connect(self.select_output_directory)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QtCore.QCoreApplication.quit)

        toolbar_layout.addWidget(screenshot_button)
        toolbar_layout.addWidget(recording_button)
        toolbar_layout.addWidget(colormap_selector)
        toolbar_layout.addWidget(output_directory_button)
        toolbar_layout.addWidget(quit_button)

        # Create a label to display the video feed
        self.label = AspectRatioLabel()

        # Add the toolbar and label to the vertical layout
        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(toolbar_widget)

        # Create a central widget and set the vertical layout as its layout
        central_widget = QWidget()
        central_widget.setLayout(vertical_layout)

        self.setCentralWidget(central_widget)

    def start_video(self):
        # Start the QTimer to update the video feed at a desired interval
        self.timer.start(30)

    def stop_video(self):
        # Stop the QTimer
        self.timer.stop()

    def update_frame(self):
        # Reading the frame using the Boson lib is currently not properly working when using on a Raspberry Pi
        # frame = self.boson.grab()
        _, frame = self.cap.read()

        frame = apply_colormap(frame, self.colormap)

        if self.recording:
            self.handle_recording(frame)

        # Create a QImage from the frame
        image = QtGui.QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QtGui.QImage.Format.Format_BGR888,
        )

        # Create a QPixmap from the QImage
        pixmap = QtGui.QPixmap.fromImage(image)

        # Set the QPixmap as the label's pixmap to display the frame
        self.label.setPixmap(pixmap)

    def closeEvent(self, event):
        # Release the VideoCapture object and stop the QTimer when the window is closed
        self.stop_video()
        event.accept()

    def change_colormap(self, colormap):
        self.colormap = colormap

    def select_output_directory(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setDirectory(self.output_directory)

        if dialog.exec():
            selected_directory = dialog.selectedFiles()
            if selected_directory:
                self.output_directory = selected_directory[0]
                self.settings.setValue("OutputDirectory", self.output_directory)

    def take_screenshot(self):
        # frame = self.boson.grab()
        _, frame = self.cap.read()

        img = apply_colormap(frame, self.colormap)

        file_path = get_file_save_path(self)
        cv2.imwrite(f"{file_path}.jpg", img)

        QtWidgets.QMessageBox.information(
            self,
            "Screenshot Saved",
            "The screenshot has been saved.",
        )

    def toggle_recording(self):
        if self.recording is False:
            self.recording = True
        else:
            self.video_writer.release()
            self.video_writer = None
            self.recording = False

    def handle_recording(self, frame):
        width = frame.shape[1]
        height = frame.shape[0]

        if self.video_writer is None:
            file_path = get_file_save_path(self)
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            self.video_writer = cv2.VideoWriter(
                f"{file_path}.mp4", fourcc, 30, (width, height)
            )

        self.video_writer.write(frame)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("../ressources/icon.ico"))
    app.setStyle(QtWidgets.QStyleFactory.create("CleanLooks"))
    window = MyWindow()
    window.show()
    window.start_video()
    sys.exit(app.exec())
