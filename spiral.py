import turtle

window = turtle.Screen()
window.bgcolor("light blue")
window.title("spiral pattern")
my_pen= turtle.Turtle()
size=0

while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
    
    size -=5