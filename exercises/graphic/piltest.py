import sys
from PIL import Image,ImageDraw,ImageDraw2

img = Image.new(mode="RGB",size=(100,100),color=(209,123,193))

img.save("output/imgtest.png")
