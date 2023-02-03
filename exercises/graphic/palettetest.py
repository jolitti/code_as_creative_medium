from PIL import Image,ImageDraw
import sys

palette = {
        "red" : (170, 57, 57),
        "light_red" : (212, 106, 106),
        "dark_red" : (128, 21, 21)
    }

border = int(sys.argv[1])

img = Image.new(mode="RGB",size=(100,100),color=palette["red"])
draw = ImageDraw.Draw(img)

draw.rectangle((border,border,100-border,100-border),fill=palette["light_red"])
draw.ellipse((border,border,100-border,100-border),fill=palette["dark_red"])

img.show()
