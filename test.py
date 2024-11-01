import random
import time
import turtle

# Parameters to set up animation
background_colour = 50, 50, 50
screen_size = 800, 800

# Create window
window = turtle.Screen()
window.tracer(0)
window.colormode(255)
window.setup(*screen_size)
window.bgcolor(background_colour)

# Create balls
balls = []

def create_new_ball():
    ball = turtle.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.pencolor("white")
    ball.setposition(
        random.randint(-screen_size[0] // 2, screen_size[0] // 2),
        random.randint(-screen_size[1] // 2, screen_size[1] // 2)
    )
    ball.setheading(random.randint(0, 359))
    ball.ball_speed = 0.5

    balls.append(ball)

create_new_ball()  # Start animation with one ball

# Main animation loop
while True:
    for ball in balls:
        # Move ball
        ball.forward(ball.ball_speed)
        # If ball goes out of bounds, move to other side
        if abs(ball.xcor()) > screen_size[0] / 2:
            ball.setx(-ball.xcor())
        if abs(ball.ycor()) > screen_size[1] / 2:
            ball.sety(-ball.ycor())

    window.update()
    time.sleep(0.001)