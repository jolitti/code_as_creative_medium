# First exercise in the "graphic" section of the book
# Objective: drawing one of every graphic primitive

# This will display a 200x600 image in the screen
# populated with several simple shapes

import sys
from PIL import Image,ImageDraw

# COLORS
white = (255,255,255)
black = (0,0,0)

# HELPER FUNCTIONS
def drawdot(draw_obj,x,y):
    draw_obj.ellipse((x-3,y-3,x+3,y+3),fill=black)

img = Image.new(mode="RGB",size=(240,720),color=white)
draw = ImageDraw.Draw(img)

draw.ellipse((10,10,110,110),outline=black,width=3)
draw.rectangle((130,10,230,110),outline=black,width=3)

drawdot(draw,10,130)
drawdot(draw,110,130)
drawdot(draw,60,230)
draw.pieslice((130,130,230,230),135,45,outline=black,width=3)

img.show()
