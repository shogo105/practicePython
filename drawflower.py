import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, r, angle, n):
    for i in range(n):
        petal(t, r, angle)
        t.rt(360 / n)

def move(t, distance):
    t.up()
    t.fd(distance)
    t.down()
    
bob = turtle.Turtle()

move(bob, -120)
flower(bob, 60.0, 60.0, 7)

move(bob, 120)
flower(bob, 40.0, 80.0, 10)

move(bob, 120)
flower(bob, 140.0, 20.0, 20)

bob.hideturtle()
turtle.mainloop()