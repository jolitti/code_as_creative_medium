import sys
from PIL import Image,ImageDraw

img = Image.new(mode="RGB",size=(100,100),color=(217, 38, 110))
draw = ImageDraw.Draw(img)

draw.ellipse([0,0,100,100], fill=(146, 37, 81))

img.save("output/imgtest.png")
