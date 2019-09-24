import turtle

def draw_multicolor_square(t,sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.speed(0)

size=20
for i in range(100):
    draw_multicolor_square(tess, size)
    size= size+1
    tess.forward(10)
    tess.right(18)

wn.mainloop()
