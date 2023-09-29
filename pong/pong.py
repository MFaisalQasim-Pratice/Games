import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Strick A
stricker_a = turtle.Turtle()
stricker_a.speed(0)
stricker_a.shape("square")
stricker_a.color("white")
stricker_a.shapesize(stretch_wid=5,stretch_len=1)
stricker_a.penup()
stricker_a.goto(-350,0)

# Strick B
stricker_b = turtle.Turtle()
stricker_b.speed(0)
stricker_b.shape("square")
stricker_b.color("white")
stricker_b.shapesize(stretch_wid=5,stretch_len=1)
stricker_b.penup()
stricker_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function
def stricker_a_up():
    y = stricker_a.ycor()
    y += 10
    stricker_a.sety(y)
    
def stricker_a_down():
    y = stricker_a.ycor()
    y -= 10
    stricker_a.sety(y)

def stricker_b_up():
    y = stricker_b.ycor()
    y += 10
    stricker_b.sety(y)
    
def stricker_b_down():
    y = stricker_b.ycor()
    y -= 10
    stricker_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(stricker_a_up,"w")
wn.onkeypress(stricker_a_down,"s")
wn.onkeypress(stricker_b_up,"Up")
wn.onkeypress(stricker_b_down,"Down")

# Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking

    #Top & Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Left & Right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal") )
        ball.goto(0,0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal") )
        ball.goto(0,0)
        ball.dx *= -1

    #Ball Bouncdes from Stricker
    if ball.xcor() < -340 and ball.ycor() < stricker_a.ycor() + 50 and ball.ycor() > stricker_a.ycor() - 50:
        ball.dx *= 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and ball.ycor() < stricker_b.ycor() + 50 and ball.ycor() > stricker_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)