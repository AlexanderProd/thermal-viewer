import cv2
from flirpy.camera.boson import Boson
from PyQt6 import QtWidgets, QtGui, QtCore

from ui.colormap_selector import ColormapSelector
from utils import apply_colormap

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 640, 512)
        self.setWindowTitle("Thermal Viewer")

        # Create a label to display the video feed
        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)

        screenshot_button = QtWidgets.QPushButton("Take Screenshot")
        screenshot_button.clicked.connect(self.take_screenshot)

        colormap_selector = ColormapSelector(self)

        main_toolbar = self.addToolBar("Main")
        main_toolbar.setMovable(False)
        main_toolbar.addWidget(screenshot_button)
        main_toolbar.addWidget(colormap_selector)

        self.boson = Boson()
        self.colormap = None

        # Create a QTimer to update the video feed
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)

    def start_video(self):
        # Start the QTimer to update the video feed at a desired interval
        self.timer.start(30)

    def stop_video(self):
        # Stop the QTimer
        self.timer.stop()

    def update_frame(self):
        # Read a frame from the webcam
        frame = self.boson.grab()

        frame = apply_colormap(frame, self.colormap)

        # Create a QImage from the frame
        image = QtGui.QImage(
            frame, 
            frame.shape[1], 
            frame.shape[0], 
            frame.strides[0], 
            QtGui.QImage.Format.Format_BGR888
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

    def take_screenshot(self):
        frame = self.boson.grab()

        img = apply_colormap(frame, self.colormap)

        cv2.imwrite("screenshot.jpg", img)

        QtWidgets.QMessageBox.information(
            self,
            "Screenshot Saved",
            "The screenshot has been saved as 'screenshot.jpg'.",
        )

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("CleanLooks"))
    window = MyWindow()
    window.show()
    window.start_video()
    sys.exit(app.exec())