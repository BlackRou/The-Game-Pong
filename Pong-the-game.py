# Simple Pong game in Python
# Odkaz: https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=3

# Part 1: Getting started
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @DronMove")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Sound files
sound_file = "bounce.wav"
sound_fail = "fail.wav"

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0    PONG    0", align="center", font=("Papyrus", 24, "normal"))



# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keybord binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}    PONG    {}".format(score_a, score_b), align="center", font=("Papyrus", 24, "normal"))
        winsound.PlaySound(sound_fail, winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}    PONG    {}".format(score_a, score_b), align="center", font=("Papyrus", 24, "normal"))
        winsound.PlaySound(sound_fail, winsound.SND_ASYNC)


    # Paddel Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)


    # Padell Collisions with wall
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)

