import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,300)

triangle=turtle.Turtle()

no_of_sides=3
side_length=100

angle=360/no_of_sides

for i in range(no_of_sides):
    triangle.forward(side_length)
    triangle.left(angle)

turtle.done()