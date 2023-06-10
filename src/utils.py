import cv2
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from datetime import datetime


def get_mpl_colormap(selected_colormap):
    cmap = None
    if type(selected_colormap["value"]) == str:
        cmap_name = selected_colormap["value"]
        cmap = plt.get_cmap(cmap_name)

    cmap = selected_colormap["value"]

    # Initialize the matplotlib color map
    sm = plt.cm.ScalarMappable(cmap=cmap)

    # Obtain linear color range
    color_range = sm.to_rgba(np.linspace(0, 1, 256), bytes=True)[:, 2::-1]

    return color_range.reshape(256, 1, 3)


def apply_colormap(frame, colormap):
    if colormap is not None:
        if colormap["type"] == "mpl":
            mpl_colormap = get_mpl_colormap(colormap)
            return cv2.applyColorMap(frame.astype(np.uint8), mpl_colormap)
        elif colormap["type"] == "cv2":
            return cv2.applyColorMap(frame.astype(np.uint8), colormap["value"])
    return frame


def get_file_save_path(self):
    folder_path = None
    if self.output_directory is None:
        folder_path = pathlib.Path.cwd()
    else:
        folder_path = pathlib.Path(self.output_directory)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{timestamp}"
    return folder_path / filename
