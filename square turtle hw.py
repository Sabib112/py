import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,300)

polygon= turtle.Turtle()

no_of_sides=4

side_length=70
angle=360/no_of_sides

for i in range(no_of_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()