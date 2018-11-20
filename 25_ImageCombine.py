from PIL import Image

img1 = Image.open("./Python/249.jpg")
img2 = Image.open("./Python/ks3.jpg")

# (startX, startY)
area = (200, 400)
# target.paste(item, position)
img2.paste(img1, area)

# Open the image
img2.show()
