from PIL import Image, ImageFilter

img = Image.open("./S17images/village.jpg")
filtered_img = img.convert("L")
filtered_img.save("./S17images/grey.png", "png")
filtered_img.show()
