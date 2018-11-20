from PIL import Image

# Open the image
img = Image.open("./Python/249.jpg")

# Resize
img_resize = img.resize((100,100))
img_resize.show()

# Flip
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flip.show()

# Rotation
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()
