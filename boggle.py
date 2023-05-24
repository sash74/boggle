import random
import turtle
a = 0
lettres= "aeuioazertyuiopqsdfghjklmwxcvbn"
turtle.speed(0)
turtle.right(90)
turtle.color("blue")
for x in range(0, 5):
  turtle.penup()
  turtle.goto(a, 250)
  turtle.pendown()
  turtle.forward(200)
  a = a + 50
b = 0
turtle.left(90)
for x in range(0, 5):
  turtle.penup()
  turtle.goto(0, a)
  turtle.pendown()
  turtle.forward(200)
  a = a - 50

turtle.color("black")
a = 10
turtle.penup()

for x in range(0, 4):
  turtle.goto(a, 190)
  turtle.write((random.choice(lettres)), font=("Arial", 48, "bold"))
  a = a + 50

a = 10
for x in range(0, 4):
  turtle.goto(a, 140)
  turtle.write((random.choice(lettres)), font=("Arial", 48, "bold"))
  a = a + 50

a = 10
for x in range(0, 4):
  turtle.goto(a, 90)
  turtle.write((random.choice(lettres)), font=("Arial", 48, "bold"))
  a = a + 50

a = 10
for x in range(0, 4):
  turtle.goto(a, 40)
  turtle.write((random.choice(lettres)), font=("Arial", 48, "bold"))
  a = a + 50

turtle.hideturtle()
turtle.done()
