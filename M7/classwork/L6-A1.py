import turtle

sc = turtle.Screen()

sc.bgcolor("pink")

sc.setup(700, 700)

turtle.title("Welcome to Turtle Graphics")

board = turtle.Turtle()
board.fillcolor("red")
board.begin_fill()
n = 10

for i in range(n):
    board.forward(100)
    board.right(360/n)
board.end_fill()
turtle.done()