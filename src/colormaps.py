import cv2
from matplotlib.colors import LinearSegmentedColormap

ironbow = LinearSegmentedColormap.from_list(
    "Ironbow",
    [(0, 0, 0), (0.13, 0, 0.55), (0.8, 0, 0.47), (1, 0.84, 0), (1, 1, 1)],
    N=100,
)
red_green_blue = LinearSegmentedColormap.from_list(
    "Red Green Blue", [(1, 0, 0), (0, 1, 0), (0, 0, 1)], N=100
)
blue_green_red = LinearSegmentedColormap.from_list(
    "Blue, Green, Red", [(0, 0, 1), (0, 1, 0), (1, 0, 0)], N=100
)
cold_red = LinearSegmentedColormap.from_list("Cold Red", [(1, 0, 0), (0, 0, 0)], N=100)
red_hot = LinearSegmentedColormap.from_list("Cold Red", [(0, 0, 0), (1, 0, 0)], N=100)
green_hot = LinearSegmentedColormap.from_list("Cold Red", [(0, 0, 0), (0, 1, 0)], N=100)
cold_red_boost = LinearSegmentedColormap.from_list(
    "Cold Red Boost", [(0.76, 0, 0), (0, 0, 0)], N=100
)
cold_green = LinearSegmentedColormap.from_list(
    "Cold Green", [(0, 1, 0), (0, 0, 0)], N=100
)
cold_green_boost = LinearSegmentedColormap.from_list(
    "Cold Green Boost", [(0, 0.76, 0), (0, 0.3, 0), (0, 0, 0)], N=100
)
hottest = LinearSegmentedColormap.from_list(
    "Hottest", [(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 0)], N=100
)

available_colormaps = {
    "default": {
        "name": "default",
        "display_name": "Default",
        "value": None,
        "type": None,
    },
    "inferno": {
        "name": "inferno",
        "display_name": "Ironbow",
        "value": cv2.COLORMAP_INFERNO,
        "type": "cv2",
    },
    "inferno_r": {
        "name": "inferno_r",
        "display_name": "Ironbow reverse",
        "value": "inferno_r",
        "type": "mpl",
    },
    "gray": {
        "name": "gray",
        "display_name": "White Hot",
        "value": None,
        "type": None,
    },
    "gray_r": {
        "name": "gray_r",
        "display_name": "Black Hot",
        "value": "gray_r",
        "type": "mpl",
    },
    "hot": {
        "name": "hot",
        "display_name": "Hot",
        "value": "hot",
        "type": "mpl",
    },
    "hot_r": {
        "name": "hot_r",
        "display_name": "Hot reverse",
        "value": "hot_r",
        "type": "mpl",
    },
    "cool": {
        "name": "cool",
        "display_name": "Cool",
        "value": "cool",
        "type": "mpl",
    },
    "cool_r": {
        "name": "cool_r",
        "display_name": "Cool reverse",
        "value": "cool_r",
        "type": "mpl",
    },
    "turbo": {
        "name": "turbo",
        "display_name": "Turbo",
        "value": "turbo",
        "type": "mpl",
    },
    "turbo_r": {
        "name": "turbo_r",
        "display_name": "Turbo reverse",
        "value": "turbo_r",
        "type": "mpl",
    },
    "jet": {
        "name": "jet",
        "display_name": "Jet",
        "value": cv2.COLORMAP_JET,
        "type": "cv2",
    },
    "jet_r": {
        "name": "jet_r",
        "display_name": "Jet reverse",
        "value": "jet_r",
        "type": "mpl",
    },
    "rainbow": {
        "name": "rainbow",
        "display_name": "Rainbow",
        "value": "rainbow",
        "type": "mpl",
    },
    "rainbow_r": {
        "name": "rainbow_r",
        "display_name": "Rainbow reverse",
        "value": "rainbow_r",
        "type": "mpl",
    },
    "red_hot": {
        "name": "red_hot",
        "display_name": "Red Hot",
        "value": red_hot,
        "type": "mpl",
    },
    "green_hot": {
        "name": "green_hot",
        "display_name": "Green Hot",
        "value": green_hot,
        "type": "mpl",
    },
    "cold_green": {
        "name": "cold_green",
        "display_name": "Cold Green",
        "value": cold_green,
        "type": "mpl",
    },
    "cold_green_boost": {
        "name": "cold_green_boost",
        "display_name": "Cold Green Boost",
        "value": cold_green_boost,
        "type": "mpl",
    },
    "cold_red": {
        "name": "cold_red",
        "display_name": "Cold Red",
        "value": cold_red,
        "type": "mpl",
    },
    "cold_red_boost": {
        "name": "cold_red_boost",
        "display_name": "Cold Red Boost",
        "value": cold_red_boost,
        "type": "mpl",
    },
    "hottest": {
        "name": "hottest",
        "display_name": "Hottest",
        "value": hottest,
        "type": "mpl",
    },
}
