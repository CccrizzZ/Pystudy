from PIL import Image

# Open the target image
img = Image.open("./Python/249.jpg")
# Get size
print(img.size)
# Get format
print(img.format)

# Open the image on computer
# Creates temp file
img.show()
