from PIL import Image,ImageDraw



# CONSTS
white = (255,255,255)
black = (0,0,0)
red = (161,0,8)
blue = (1,51,148)
yellow = (240,211,93)

imgsize = 1000
origimgsize = 375

# reference img: 375x375
# rectangles: (x_upperleft,y_upperleft,width,height,color)
red_rect = (0,0,92,113,red)
blue_rect = (0,275,92,103,blue)
yellow_rect = (336,275,41,103,yellow)
bar1 = (92,0,10,375,black)
bar2 = (0,265,375,10,black)
bar3 = (0,112,92,18,black)
bar4 = (326,270,10,113,black)

rectangles = {red_rect,blue_rect,yellow_rect,bar1,bar2,bar3,bar4}

img = Image.new(size=(imgsize,imgsize),color=white,mode="RGB")
draw = ImageDraw.Draw(img)

# relative box
def rect(rectdata:tuple):
    ratio = imgsize/origimgsize
    x,y,dx,dy,color = rectdata
    x,y,dx,dy = map(lambda x:x*ratio,(x,y,dx,dy))
    draw.rectangle((x,y,x+dx,y+dy),fill=color)

for r in rectangles: rect(r)

# img.show()
img.save("output/coding_mondrian.png","PNG")
