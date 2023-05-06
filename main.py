import cv2
from flirpy.camera.boson import Boson
from PyQt6 import QtWidgets, QtGui, QtCore
import numpy as np

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 640, 512)
        self.setWindowTitle("Thermal Viewer")

        # Create a label to display the video feed
        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)

        self.screenshot_button = QtWidgets.QPushButton("Take Screenshot")
        self.screenshot_button.clicked.connect(self.take_screenshot)

        colormap_button = QtWidgets.QPushButton("Change Colormap")
        colormap_button.clicked.connect(self.change_colormap)

        self.addToolBar("Main").addWidget(self.screenshot_button)
        self.addToolBar("Main").addWidget(colormap_button)

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

        frame = self.apply_colormap(frame)

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

    def apply_colormap(self, frame):
        if self.colormap is not None:
            return cv2.applyColorMap(frame.astype(np.uint8), self.colormap)
        return frame

    def take_screenshot(self):
        frame = self.boson.grab()

        img = self.apply_colormap(frame)

        cv2.imwrite("screenshot.jpg", img)

        QtWidgets.QMessageBox.information(
            self,
            "Screenshot Saved",
            "The screenshot has been saved as 'screenshot.jpg'.",
        )

    def change_colormap(self):
        self.colormap = cv2.COLORMAP_INFERNO

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("CleanLooks"))
    window = MyWindow()
    window.show()
    window.start_video()
    sys.exit(app.exec())