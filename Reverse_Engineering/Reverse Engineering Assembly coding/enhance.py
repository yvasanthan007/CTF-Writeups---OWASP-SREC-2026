from PIL import Image, ImageOps, ImageEnhance

im = Image.open("code.png").convert("RGB")

# Increase local visibility through contrast stretching
gray = ImageOps.grayscale(im)
ImageOps.autocontrast(gray).save("code_contrast.png")

# Inspect individual color channels
for name, channel in zip(("red", "green", "blue"), im.split()):
    ImageOps.autocontrast(channel).save(f"code_{name}.png")

# Rotate to inspect the bands in the other direction
ImageOps.autocontrast(gray.rotate(90, expand=True)).save("code_rotated.png")

print("Created enhanced images.")
