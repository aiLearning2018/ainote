import turtle

def draw_square(angle):
    t = turtle.Turtle()
    t.right(angle)
    t.speed("fast")

    for i in range(1, 5):
        t.right(90)
        t.fd(100)


def draw_image():
    for i in range(0, 360, 10):
        draw_square(i)

draw_image()
