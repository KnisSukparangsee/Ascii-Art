from PIL import Image
import numpy as np
from colorama import Fore, init
import sys

def average(r, g, b):
    return (int(r) + int(g) + int(b))/3


def min_max(r, g, b):
    return (max(int(r), int(g), int(b)) + min(int(r), int(g), int(b))) / 2

def luminosity(r, g, b):
    return (0.21 * int(r) + 0.72 * int(g) + 0.07 * int(b))


def grayscale(r, g, b):
    return int(0.299 * int(r) + 0.587 * int(g) + 0.114 * int(b))


def assign_char(x, ascii):
    idx = int((x / 255) * (len(ascii) - 1))
    return ascii[idx]


def dark_version(x):
    return 255 - x

init(autoreset=True)

im = Image.open(f"{sys.argv[1]}.jpg")
im_width, im_height = im.size
aspect_ratio = im_width / im_height
new_height = 150
new_width = int(new_height * aspect_ratio)
dim = (new_width, new_height)
im = im.resize(dim, Image.Resampling.LANCZOS)

array = np.asarray(im)
height, width, _ = array.shape

brightness = np.zeros((height,width))

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

colors = [Fore.BLACK, Fore.BLUE, Fore.RED, Fore.MAGENTA, Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.WHITE]

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
        elif alg == "col":
            lux = grayscale(r, g, b)
        if len(sys.argv) == 4 and sys.argv[3] == "dark":
            lux = dark_version(lux)
        brightness[row][col] = lux

        for i in range(2):
            print(colors[int(lux / 32)] + assign_char(lux, ascii), end='')
    print()
