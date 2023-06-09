import cv2
from PyQt6.QtWidgets import QComboBox

from colormaps import available_colormaps


class ColormapSelector(QComboBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setGeometry(50, 50, 150, 30)

        display_names = [
            colormap["display_name"] for colormap in available_colormaps.values()
        ]
        self.addItems(display_names)

        self.currentIndexChanged.connect(self.on_index_changed)

    def on_index_changed(self, index):
        self.itemText(index)

        selected_colormap = list(available_colormaps.items())[index][1]

        # The parent of the ColormapSelector is the MainToolbar
        parent = self.parent().parent()
        if parent:
            parent.change_colormap(selected_colormap)
