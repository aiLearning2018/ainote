import turtle

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



c = turtle.Turtle()
c.shape("triangle")
c.color("yellow", "blue")
c.speed("slowest")
c.circle(100)

a = turtle.Turtle()
a.fd(100)
a.right(120)
a.fd(100)
a.right(120)
a.fd(100)


s = t.getscreen()
s.exitonclick()

