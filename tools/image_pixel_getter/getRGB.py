from PIL import Image

im = Image.open("Capture.JPG")
pix = im.load()
print im.size
print pix[1,1]
