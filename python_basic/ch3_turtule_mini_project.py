import turtle

def draw_fill_triangle(t, length, degree):
    for i in range(1, 4):
        t.begin_fill()
        t.fd(length)
        t.left(degree)
        t.fd(length)
        t.end_fill()

def move_turtle(t, length):
    t.fd(length)

def rotate_move_turtle(t, length, degree):
    t.penup()
    t.right(degree)
    move_turtle(t, length)
    t.left(degree)

def draw_fractal(t, length, degree):
    draw_fill_triangle(t, length, degree)

    move_len = 2 * length
    rotate_move_turtle(t, move_len, degree)

    draw_fill_triangle(t, length, degree)

    t.fd(move_len)
    draw_fill_triangle(t, length, degree)

def new_turtle(co, sp, sh):
    t = turtle.Turtle()
    t.shape(sh)
    t.color(co)
    t.speed(sp)
    return t

def draw_fractals():
    t = new_turtle("green", "fastest", "turtle")

    t.fill(True)
    t.fillcolor("green")

    draw_fractal(t, 20, 120)

    rotate_move_turtle(t, 40, 120)
    rotate_move_turtle(t, 40, 180)
    draw_fractal(t, 20, 120)

    rotate_move_turtle(t, 40, 240)
    move_turtle(t, 80)
    draw_fractal(t, 20, 120)


def draw_flower():
    t = new_turtle("blue", "fastest", "turtle")
    rotate_move_turtle(t, 300, 180)

    t.pendown()
    for i in range(0, 90):
        t.right(4)
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
    t.right(90)
    t.fd(300)
    pass

def write_initials():
    t = new_turtle("blue", "fastest", "turtle")

    rotate_move_turtle(t, )

    t.right(90)
    t.fd(200)
    t.back(100)
    t.left(45)
    t.fd(140)
    t.back(140)
    t.left(90)
    t.fd(140)

    t.right(45)
    rotate_move_turtle(t, 80, 0)
    t.pendown()

    t.back(60)
    t.right(90)
    t.fd(200)
    t.left(90)
    t.fd(60)

    s = t.getscreen()
    s.exitonclick()
    pass

# draw a fractals in the middle, a flower on the left, and write an initials on the right.
draw_fractals()
draw_flower()
write_initials()