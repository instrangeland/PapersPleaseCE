from PIL import Image

im = Image.open("Capture.JPG")
pix = im.load()
for i in range(1,im.size[0]+1):
		for j in range(1,im.size[1]+1):
			print(pix[i,j][0])
			print(",")
			print(pix[i,j][1])
			print(",")
			print(pix[i,j][2])
			print(":")