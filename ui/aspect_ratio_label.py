from PyQt6.QtWidgets import QLabel


class AspectRatioLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)  # Enable scaling of the label's content

    def resizeEvent(self, event):
        # Get the current size of the label
        current_size = self.size()

        # Get the original pixmap (assumed to be set using setPixmap())
        pixmap = self.pixmap()

        if pixmap.isNull():
            return

        # Calculate the aspect ratio
        aspect_ratio = pixmap.width() / pixmap.height()

        # Calculate the new width based on the current height
        new_width = current_size.height() * aspect_ratio

        # Set the new size
        self.setFixedSize(new_width, current_size.height())
