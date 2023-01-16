import turtle
t = turtle.Turtle()

# make square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# make roof
t.goto(50,50)
t.goto(100,0)

# go to and make door
t.goto(100,-100)
t.goto(55,-100)
t.goto(55,-80)
t.goto(45,-80)
t.goto(45,-100)

# make path
t.goto(0,-400)
t.goto(34,-400)
t.goto(55,-100)

# make 3d 
t.goto(120,-100)
t.goto(122,0)
t.goto(100,0)
t.goto(50,50)
t.goto(75,50)
t.goto(122,0)


input("Press any key to exit ...")