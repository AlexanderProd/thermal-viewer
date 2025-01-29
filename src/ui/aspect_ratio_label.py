from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt


class AspectRatioLabel(QLabel):
    clicked = pyqtSignal()  # Signal to emit when label is clicked

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(640)  # Set minimum width only
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._pixmap = None

    def setPixmap(self, pixmap):
        self._pixmap = pixmap
        self._updatePixmap()

    def _updatePixmap(self):
        if self._pixmap and not self._pixmap.isNull():
            scaled_pixmap = self._pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            super().setPixmap(scaled_pixmap)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._updatePixmap()
