from PIL import Image
import numpy as np
from colorama import Fore, init
import sys

"""Functions for calculating color brightness"""


def average(r, g, b):
    """Returns average of the RGB values"""
    return (int(r) + int(g) + int(b)) / 3


def min_max(r, g, b):
    """Returns average of max and min of RGB values"""
    return (max(int(r), int(g), int(b)) + min(int(r), int(g), int(b))) / 2


def luminosity(r, g, b):
    """Adjusts color based on perceived brightness based on the human eye"""
    return 0.21 * int(r) + 0.72 * int(g) + 0.07 * int(b)


"""Function for choosing color"""


def assign_char(x, ascii):
    idx = int((x / 255) * (len(ascii) - 1))
    return ascii[idx]


"""Function for inverting color"""


def dark_version(x):
    return 255 - x


"""Resets terminal color"""
init(autoreset=True)

"""Converts image to pillow Image with same aspect ratio"""
im = Image.open(f"{sys.argv[1]}.jpg")
im_width, im_height = im.size
aspect_ratio = im_width / im_height
new_height = 100
new_width = int(new_height * aspect_ratio * 2.4)
dim = (new_width, new_height)
im = im.resize(dim, Image.Resampling.LANCZOS)

"""Initialize empty 2d array to store lux"""
array = np.asarray(im)
height, width, _ = array.shape
brightness = np.zeros((height, width))

"""String to store ASCII characters in ascending order based on density"""
ascii = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

"""Array of colors"""
colors = [
    Fore.BLACK,
    Fore.BLUE,
    Fore.RED,
    Fore.MAGENTA,
    Fore.GREEN,
    Fore.CYAN,
    Fore.YELLOW,
    Fore.WHITE,
]

"""Prints the ascii art"""
for row in range(height):
    for col in range(width):
        r, g, b = array[row][col][:3]
        alg = sys.argv[2]
        if alg == "ave":
            lux = average(r, g, b)
        elif alg == "minmax":
            lux = min_max(r, g, b)
        elif alg == "lum":
            lux = luminosity(r, g, b)
        if len(sys.argv) == 4 and sys.argv[3] == "dark":
            lux = dark_version(lux)
        brightness[row][col] = lux

        for i in range(1):
            print(colors[int(lux / 32)] + assign_char(lux, ascii), end="")
    print()
