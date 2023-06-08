import cv2
import numpy as np
import pathlib
from datetime import datetime


def apply_colormap(frame, colormap):
    if colormap is not None:
        return cv2.applyColorMap(frame.astype(np.uint8), colormap)
    return frame


def get_file_save_path(self):
    home_dir = pathlib.Path.home()
    video_dir = home_dir / "Videos"
    folder_name = "thermal-viewer"
    folder_path = video_dir / folder_name

    if not folder_path.exists():
        try:
            folder_path.mkdir(parents=True)
        except OSError as e:
            print(f"Error creating folder: {e}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{timestamp}"
    return folder_path / filename
