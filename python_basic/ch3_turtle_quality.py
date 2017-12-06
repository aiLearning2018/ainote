import turtle

def draw_square():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red", "green")
    t.speed("slow")

    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    listen_exit(t)


def draw_circle():
    c = turtle.Turtle()
    c.shape("triangle")
    c.color("yellow", "blue")
    c.speed("slowest")
    c.circle(100)

def draw_triangle():
    a = turtle.Turtle()
    a.fd(100)
    a.right(120)
    a.fd(100)
    a.right(120)
    a.fd(100)

def listen_exit(t):
    s = t.getscreen()
    s.exitonclick()

def run_turtle():
    draw_square()
    draw_circle()
    draw_triangle()
