import turtle
import math

bob = turtle.Turtle()

#draw(bob, 半径rの円, n角形)
def draw(t, r, n):
    
    t.lt(360.0/n)
    #円に接している側の三角形の内角
    angle = 180.0-(180.0-(360.0/n))/2
    
    t.up()
    for i in range(n):
        t.fd(r)
        t.lt(angle)
        t.down()
        t.fd(math.sqrt(r**2+r**2-2*r**2*math.cos((360.0/n)*math.pi/180)))
        t.lt(angle)
        t.fd(r)
        t.up()
        t.lt(180.0)
    
    t.rt(360.0/n)

def move(t, distance):
    t.up()
    t.fd(distance)
    t.down()
    
move(bob, -120)
draw(bob, 50.0, 5)

move(bob, 120)
draw(bob, 50.0, 6)

move(bob, 120)
draw(bob, 50.0, 7)

bob.hideturtle()
turtle.mainloop()