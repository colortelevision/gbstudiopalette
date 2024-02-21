from PIL import Image

palette_colors = [
    (15, 56, 15),
    (48, 98, 48),
    (139, 172, 15),
    (155, 188, 15),
]

img = Image.new("RGB", (4, 1))

for i, color in enumerate(palette_colors):
    img.putpixel((i, 0), color)

img.save("custom_palette.png")

