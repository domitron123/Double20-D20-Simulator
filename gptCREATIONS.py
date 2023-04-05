# import turtle
# import random

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("#2c3e50")

# # Define the possible colors and petal shapes
# colors = ["#f7dc6f", "#f5b041", "#eb984e", "#e67e22"]
# petals = [3, 4, 5, 6, 7, 8]

# # Define the size of the flowers
# size = 20

# # Draw the pattern
# for i in range(75):
#     # Move the turtle to a random position on the screen
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()

#     # Draw a flower with a random color and petal shape
#     color = random.choice(colors)
#     petal_shape = random.choice(petals)
#     t.color(color)
#     t.begin_fill()
#     for j in range(petal_shape):
#         t.forward(size)
#         t.right(360/petal_shape)
#     t.end_fill()

#     # Draw the center of the flower
#     t.color("#34495e")
#     t.begin_fill()
#     t.circle(size/3)
#     t.end_fill()

#     # Draw the stem and leaves of the flower
#     t.right(90)
#     t.color("#52be80")
#     t.begin_fill()
#     t.forward(size*2)
#     t.right(90)
#     t.forward(size/2)
#     t.right(90)
#     t.forward(size)
#     t.left(90)
#     t.forward(size/2)
#     t.left(90)
#     t.forward(size*2)
#     t.end_fill()

# # Hide the turtle and exit the program
# t.hideturtle()
# turtle.done()







# import turtle
# import random

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("#2c3e50")

# # Define the possible colors and petal shapes
# colors = ["#f7dc6f", "#f5b041", "#eb984e", "#e67e22"]
# petals = [3, 4, 5, 6, 7, 8]

# # Define the size of the flowers
# size = 20

# # Draw the head of the dog
# t.penup()
# t.goto(-50, 50)
# t.pendown()
# t.color("#bdc3c7")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# # Draw the eyes
# t.penup()
# t.goto(-30, 70)
# t.pendown()
# t.color("black")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# t.penup()
# t.goto(10, 70)
# t.pendown()
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# # Draw the nose
# t.penup()
# t.goto(-10, 30)
# t.pendown()
# t.color("#ecf0f1")
# t.begin_fill()
# t.circle(15)
# t.end_fill()

# # Draw the ears
# t.penup()
# t.goto(-80, 90)
# t.pendown()
# t.color("#bdc3c7")
# t.begin_fill()
# t.right(30)
# t.forward(60)
# for i in range(3):
#     t.right(60)
#     t.forward(30)
# t.right(60)
# t.forward(60)
# t.end_fill()

# t.penup()
# t.goto(30, 90)
# t.pendown()
# t.begin_fill()
# t.left(30)
# t.forward(60)
# for i in range(3):
#     t.left(60)
#     t.forward(30)
# t.left(60)
# t.forward(60)
# t.end_fill()

# # Draw the body
# t.penup()
# t.goto(-90, -20)
# t.pendown()
# t.color("#bdc3c7")
# t.begin_fill()
# t.forward(120)
# t.right(120)
# t.forward(100)
# t.right(60)
# t.forward(120)
# t.end_fill()

# # Draw the legs
# for i in range(4):
#     t.penup()
#     t.goto(-90 + 60 * i, -20)
#     t.pendown()
#     t.color("#bdc3c7")
#     t.begin_fill()
#     t.forward(40)
#     t.right(90)
#     t.forward(80)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(80)
#     t.end_fill()

# # Draw the flowers on the body
# for i in range(25):
#     # Move the turtle to a random position on the dog's body
#     x = random.randint(-70, 70)
#     y = random.randint(-40, 70)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()

#     # Draw a flower with a random color and petal shape
#     color = random.choice(colors)
#     petal_shape = random.choice(petals)
#     t.color(color)
#     t.begin_fill()
#     for j in range(petal_shape):
#         t.forward(size)
#         t.right(360/petal_shape)
#     t.end_fill()

# # Hide the turtle and keep the window open
# t.hideturtle()
# turtle.done()




#ANCHOR import turtle
# import random

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("#000000")
# turtle.tracer(0)

# # Define the number of points and size of the loop
# points = 150
# size = 400
# angle = 60

# # Draw the loop
# for i in range(points):
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()

#     # Set the color of the curve
#     while True:
#         try:
#             color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             t.pencolor(color)
#             break
#         except turtle.TurtleGraphicsError:
#             pass

#     # Set the fill color of the curve
#     while True:
#         try:
#             fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             t.fillcolor(fill_color)
#             break
#         except turtle.TurtleGraphicsError:
#             pass

#     # Generate the curve
#     t.begin_fill()
#     t.setheading(i * 360/points)
#     t.circle(size, angle + random.randint(-90, 90))
#     t.left(120 + random.randint(-60, 60))
#     t.circle(size, angle + random.randint(-90, 90))
#     t.left(120 + random.randint(-60, 60))
#     t.end_fill()

#     # Randomly add stars
#     if random.random() < 0.2:
#         t.penup()
#         x = random.randint(-400, 400)
#         y = random.randint(-400, 400)
#         t.goto(x, y)
#         t.pendown()
#         t.dot(5, "#FFFFFF")

# # Hide the turtle and update the screen
# t.hideturtle()
# turtle.update()
# turtle.done()




import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")
turtle.bgcolor("#000000")

# Set up the turtle window
wn = turtle.Screen()
wn.delay(0)

# Define the number of points and size of the loop
points = 25
size = 300

# Draw the loop
for i in range(points):
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Set the color of the curve
    while True:
        try:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            t.pencolor(color)
            break
        except turtle.TurtleGraphicsError:
            pass

    # Set the fill color of the curve
    while True:
        try:
            fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            t.fillcolor(fill_color)
            break
        except turtle.TurtleGraphicsError:
            pass

    # Generate the curve
    t.begin_fill()
    t.setheading(i * 360 / points)
    for j in range(3):
        t.circle(size, random.randint(50, 100))
        t.left(120)
    t.end_fill()

    # Update the turtle window
    wn.update()

    # Randomly add stars
    if random.random() < 0.05:
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x, y)
        t.pendown()
        t.dot(5, "#FFFFFF")

# Hide the turtle and update the screen
t.hideturtle()
wn.update()
turtle.done()

