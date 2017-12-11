import turtle

t = turtle.Turtle()
s = t.getscreen()

s.register_shape("turtle_shape_rabbit.gif")
t.shape("turtle_shape_rabbit.gif")

t.fd(100)
t.left(90)
t.fd(100)

s.exitonclick()
