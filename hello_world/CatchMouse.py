import turtle
import time
import this

boxsize = 200
caught = False
score = 0

#functions Keypress
def up():
    mouse.forward(10)
    checkbound()
def down():
    mouse.backward(10)
    checkbound()
def left():
    mouse.left(45)
def right():
    mouse.right(45)
def quitTurtles():
    window.bye()

#limit box
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize :
        mouse.goto(boxsize,mouse.ycor())
    if mouse.xcor() < -boxsize :
        mouse.goto(-boxsize,mouse.ycor())
    if mouse.ycor() > boxsize :
        mouse.goto(mouse.xcor(),boxsize)
    if mouse.ycor() < -boxsize :
        mouse.goto(mouse.xcor(),-boxsize)

#set screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100,100)

#add key listen
window.onkeypress(up,"Up")
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")
window.onkeypress(down,"Down")
window.onkeypress(quitTurtles,"Escape")
difficulty = window.numinput("Difficulty","Enter a difficulty form easy(1) or hard(5)",minval=1,maxval=5)

window.listen()
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8+difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2-(0.01*difficulty))
window.textinput("GAME OVER","well done! your score :"+str(score*difficulty))
window.bye()


