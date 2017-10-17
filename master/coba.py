from PIL import Image

im = Image.open("./img/Gu Office.PNG")

print(im.format,im.size,im.mode)
im.show()