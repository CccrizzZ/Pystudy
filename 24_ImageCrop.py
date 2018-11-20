from PIL import Image

img = Image.open("./Python/249.jpg")
# Setting areas (startX, startY, endX, endY)
area = (0, 0, 200, 100)
cropped_img = img.crop(area)

# Open the image
cropped_img.show()
