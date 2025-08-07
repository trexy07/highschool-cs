from PIL import Image


## makes list of rgb binary values from an image


# Open the BMP image
# img = Image.open("New Project (2).bmp")
img = Image.open("new.bmp")
pixels = img.load()

width, height = img.size

pixels = list(img.getdata())
for pixel in pixels:
    r, g, b = pixel[:3]
    value = (r << 16) | (g << 8) | b
    print(f"{value:024b}")
    with open("pixel_values.txt", "a") as f:
        f.write(f"{value:024b}\n")