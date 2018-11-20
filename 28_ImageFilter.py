from PIL import Image
from PIL import ImageFilter

img = Image.open("./Python/ks3.jpg")

# Black and white filter
black_white = img.convert("L")
black_white.show()

# Blur filter
blur = img.filter(ImageFilter.BLUR)
blur.show()
