import turtle
pen = turtle.Screen()
pen.bgcolor("pink")
pen.title("spiral pettern")
cursor = turtle.Turtle()
size = 0
while True:
    for i in  range(4):
        cursor.fd(size+1)
        cursor.left(90)
        size = size - 5
    size = size + 1