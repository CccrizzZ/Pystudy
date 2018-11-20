from PIL import Image

img = Image.open("./Python/249.jpg")
img2 = Image.open("./Python/ks3.jpg")
# Image size have to be same
img3 = img2.crop((0,0,573,300))
# Current color mode of the image
print(img.mode)
# Get rgb channels
r, g, b = img.split()
r1, g1, b1 = img3.split()

# Merge Effect
new_img = Image.merge("RGB", (b,g,r))
new_img.show()

new_img2 = Image.merge("RGB", (r, g1, b))
new_img2.show()
