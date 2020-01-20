# Simple Pong in Python 3

import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_speed = 0.3

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.dy = paddle_speed


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.dy = paddle_speed

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0   Player B: 0", align="center", font=("Impact", 28, "normal"))

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() - ball.dy)

    # Move the paddles
    paddle_a.sety(paddle_a.ycor() + paddle_a.dy)
    paddle_b.sety(paddle_b.ycor() + paddle_b.dy)

    # Paddle A
    def paddle_a_up():
        if paddle_a.dy < 0:
            paddle_a.dy *= -1
        if paddle_a.dy == 0:
            paddle_a.dy = paddle_speed

    def paddle_a_down():
        if paddle_a.dy > 0:
            paddle_a.dy *= -1
        if paddle_a.dy == 0:
            paddle_a.dy = - paddle_speed

    # Paddle B
    def paddle_b_up():
        if paddle_b.dy < 0:
            paddle_b.dy *= -1
        if paddle_b.dy == 0:
            paddle_b.dy = paddle_speed

    def paddle_b_down():
        if paddle_b.dy > 0:
            paddle_b.dy *= -1
        if paddle_b.dy == 0:
            paddle_b.dy = - paddle_speed

    # Keyboard binding
    win.listen()
    win.onkeypress(paddle_a_up, "w")
    win.onkeypress(paddle_a_down, "s")
    win.onkeypress(paddle_b_up, "Up")
    win.onkeypress(paddle_b_down, "Down")

    # Paddle border check
    if paddle_a.ycor() > 260:
        paddle_a.sety(260)
        paddle_a.dy = 0

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)
        paddle_a.dy = 0

    if paddle_b.ycor() > 260:
        paddle_b.sety(260)
        paddle_b.dy = 0

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)
        paddle_b.dy = 0

    # Ball border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Impact", 28, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Impact", 28, "normal"))

    # Paddle/Ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
