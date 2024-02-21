from PIL import Image
import numpy as np

# Open the image file
img = Image.open("image.png").convert('RGB')
pixels = np.array(img)

# Define the original and new color palettes
original_palette = np.array([[0, 0, 0], [85, 85, 85], [170, 170, 170], [255, 255, 255]])
new_palette = np.array([[7, 24, 33], [134, 192, 108], [224, 248, 207], [0, 255, 0]])

# Tolerance for color matching
tolerance = 30

# Replace the colors
for x in range(pixels.shape[0]):
    for y in range(pixels.shape[1]):
        color = pixels[x, y]
        diff = np.sqrt(np.sum((original_palette - color)**2, axis=1))
        closest_color_index = np.argmin(diff)
        if diff[closest_color_index] <= tolerance:
            pixels[x, y] = new_palette[closest_color_index]

# Convert array back to Image and save
img_with_new_palette = Image.fromarray(pixels)
img_with_new_palette.save("image_with_new_palette.png")
