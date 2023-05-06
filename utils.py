import cv2
import numpy as np

def apply_colormap(frame, colormap):
    if colormap is not None:
        return cv2.applyColorMap(frame.astype(np.uint8), colormap)
    return frame