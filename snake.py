import turtle
import time
import random

# Score and delay
score = 0
high_score = 0
delay = 0.05  # Reduced delay for smoother movement

# Set up the screen
wn = turtle.Screen()
wn.title('Snake Game by Aryan')
wn.bgcolor("white")
wn.setup(width=700, height=700)
wn.tracer(0)  # Turns off screen updates

# Outline of the playing field
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('square')
pencil.color('black')
pencil.penup()
pencil.hideturtle()
pencil.goto(345, 345)
pencil.pendown()
pencil.goto(-345, 345)
pencil.goto(-345, -345)
pencil.goto(345, -345)
pencil.goto(345, 345)
pencil.penup()

# Snake head
head = turtle.Turtle()
head.speed(1)
head.shape("square")
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('grey')
food.penup()
food.goto(0, 100)

# Contains information about snake body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align='center', font=('Courier', 24, 'normal'))

# Function to update the score
def update_score():
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

# Functions that move snake in response to keyboard keys
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Function that helps the snake move
def move():
    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    # Keep the snake moving in the same direction
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)

# Function that tells the game what to do when collision occurs
def collision():
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = 'stop'
    # Hide the segments
    for segment in segments:
        segment.hideturtle()
    # Clear the segments list
    segments.clear()
    global score, delay
    score = 0
    delay = 0.05  # Reset the delay
    update_score()

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_up, 'w')

wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_down, 's')

wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_left, 'a')

wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_right, 'd')

# Loop that runs the game code
while True:
    wn.update()

    # Check for collision with border
    if head.xcor() > 327 or head.xcor() < -327 or head.ycor() > 327 or head.ycor() < -327:
        collision()

    # Check if the snake eats the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        food.goto(random.randint(-327, 327), random.randint(-327, 327))
        
        # Add a segment with a 2.5px space
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("black")
        new_segment.penup()
        
        # Set the new segment position slightly behind the last segment
        if segments:
            last_segment = segments[-1]
            new_x = last_segment.xcor()
            new_y = last_segment.ycor()
            # Determine the direction to offset based on the snake's direction
            if head.direction == 'up':
                new_y -= 5
            elif head.direction == 'down':
                new_y += 5
            elif head.direction == 'left':
                new_x += 5
            elif head.direction == 'right':
                new_x -= 5
            new_segment.goto(new_x, new_y)
        else:
            # If it's the first segment, place it directly at the head's position
            new_segment.goto(head.xcor(), head.ycor())
        
        segments.append(new_segment)
        
        # Shorten the delay - this increases speed of snake as it gets longer
        delay -= 0.001
        
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move the snake in the game
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 10:
            collision()

    time.sleep(delay)

# Makes the window visible and runs everything
wn.mainloop()
