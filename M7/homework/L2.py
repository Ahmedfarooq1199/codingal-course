import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Turtle Drawing Demo")
screen.bgcolor("black")
screen.colormode(255)   # allow RGB 0–255

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Spiral drawing
def draw_spiral():
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(200):
        pen.pencolor((i*3) % 256, (i*7) % 256, (i*11) % 256)
        pen.forward(i * 2 / 3)
        pen.right(25)

# Star drawing
def draw_star(x, y, size=120, points=5):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(-90)
    pen.pencolor(255, 215, 0)
    for i in range(points * 2):
        if i % 2 == 0:
            pen.forward(size)
        else:
            pen.forward(size / 2)
        pen.right(180 - (180 / points))

# Squares drawing
def draw_squares(x, y, size=200, count=6):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for i in range(count):
        pen.pencolor((i*40) % 256, (i*70) % 256, (i*90) % 256)
        for _ in range(4):
            pen.forward(size)
            pen.right(90)
        pen.right(15)
        size -= 20

# Save snapshot
def save_snapshot():
    filename = f"turtle_{int(time.time())}.ps"
    screen.getcanvas().postscript(file=filename)
    print("Saved:", filename)

# Quit program
def quit_program():
    turtle.bye()

# Clear and redraw everything
def reset_drawing():
    pen.clear()
    draw_spiral()
    draw_star(-200, 150, 100, 5)
    draw_star(200, -150, 80, 7)
    draw_squares(-100, -50, 160, 8)

# Key bindings
screen.listen()
screen.onkey(reset_drawing, "c")
screen.onkey(save_snapshot, "s")
screen.onkey(quit_program, "q")

# First draw
reset_drawing()

turtle.done()
