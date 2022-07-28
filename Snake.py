# Snake

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Setup the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #Turns off sceen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Pen for delay
pen_delay = turtle.Turtle()
pen_delay.speed(0)
pen_delay.shape("square")
pen_delay.color("white")
pen_delay.penup()
pen_delay.hideturtle()
pen_delay.goto(0, 240)
pen_delay.write("Delay = 0.1", align="center", font=("Courier", 20, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

# Main game loop
while True:
    window.update()

    # Check for a collision with border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset score
        score = 0

        # Reset delay
        delay = 0.1

        pen_delay.clear()
        pen_delay.write("Delay = {}".format(delay), align="center", font=("Courier", 24, "normal"))

        # Update the score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        while x % 20 != 0: # Add 1 until random x-number is aligned in the size-20 grid
            x += 1
        y = random.randint(-280, 280)
        while y % 20 != 0: # Add 1 until random y-number is aligned
            y += 1
        food.goto(x, y)

        # Add a segment to the snake head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        pen_delay.clear()
        pen_delay.write("Delay = {}".format(delay), align="center", font=("Courier", 24, "normal"))

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the sneak head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset score
            score = 0

            # Reset delay
            delay = 0.1

            pen_delay.clear()
            pen_delay.write("Delay = {}".format(delay), align="center", font=("Courier", 24, "normal"))

            # Update the score display
            pen.clear()
            pen.write("Score: {}  Hight Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

window.mainloop()