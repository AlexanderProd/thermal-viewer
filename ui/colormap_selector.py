import cv2
from PyQt6.QtWidgets import QComboBox

colormaps = {
    "Default": None,
    "Bone": cv2.COLORMAP_BONE,
    "Jet": cv2.COLORMAP_JET,
    "Inferno": cv2.COLORMAP_INFERNO,
    "Magma": cv2.COLORMAP_MAGMA,
    "Plasma": cv2.COLORMAP_PLASMA,
    "Rainbow": cv2.COLORMAP_RAINBOW,
    "Viridis": cv2.COLORMAP_VIRIDIS,
    "Autumn": cv2.COLORMAP_AUTUMN,
    "Cool": cv2.COLORMAP_COOL,
    "Hot": cv2.COLORMAP_HOT,
    "HSV": cv2.COLORMAP_HSV,
    "Spring": cv2.COLORMAP_SPRING,
    "Summer": cv2.COLORMAP_SUMMER,
    "Winter": cv2.COLORMAP_WINTER,
}

class ColormapSelector(QComboBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setGeometry(50, 50, 150, 30)

        colormap_list = list(colormaps.keys())
        self.addItems(colormap_list)

        self.currentIndexChanged.connect(self.on_index_changed)

    def on_index_changed(self, index):
        selected_item = self.itemText(index)

        colormap = colormaps[selected_item]

        # The parent of the ColormapSelector is the MainToolbar
        parent = self.parent().parent()
        if parent:
            parent.change_colormap(colormap)