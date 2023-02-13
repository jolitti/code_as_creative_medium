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

draw.arc((10,250,110,350),180,290,fill="black",width=3)
draw.chord((130,250,230,350),290,180,outline=black,width=3)

draw.polygon((120,470,70,400,70,370,100,370,120,390,140,370,170,370,170,400),outline=black,width=3)
draw.line((30,410,120,470,210,410),fill=black,width=3)

# Absolutely hideous hack to get a width 3 regular polygon
for i in [-1,0,1]:
    for j in [-1,0,1]:
        draw.regular_polygon((60+i,540+j,50),5,outline=black)
        draw.regular_polygon((180+i,540+j,50),7,outline=black)

draw.rounded_rectangle((10,610,230,710),radius=10,outline=black,width=3)

img.show()
img.save("output/one_with_everything.png","PNG")
