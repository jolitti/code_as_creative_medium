from PIL import Image, ImageDraw

# DRAW OBJ CREATION
img = Image.new(mode="RGB",size=(310,160),color="white")
draw = ImageDraw.Draw(img)

# E
draw.polygon((20,20,140,20,20,60),outline="black",width=3)
draw.polygon((20,140,140,140,140,100),outline="black",fill="grey",width=3)
draw.polygon(
        (20,80,20,120,140,80,140,40),
        outline="black",fill="lightgrey",width=3
        )

# G
draw.pieslice(
        (160,20,280,140),
        outline="black",fill="grey",
        width=3,
        start=90,end=270
        )
draw.pieslice(
        (160+10,20,280+10,140),
        outline="black",fill="black",
        width=3,
        start=0,end=90
        )
draw.arc(
        (160+10,20,280+10,140),
        fill="black",width=5,
        start=270,end=270+60
        )

# img.show()
img.save("output/draw_your_initials.png")
