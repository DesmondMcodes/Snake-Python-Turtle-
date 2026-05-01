from turtle import *
import random
import time


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.shape("square")
    self.color("black")
    self.pu()
    self.alive = True
    self.direction = ""
    screen.onkey(self.left, "Left")
    screen.onkey(self.right, "Right")
    screen.onkey(self.up, "Up")
    screen.onkey(self.down, "Down")
    self.speed(0)

  def up(self):
    if self.heading() != 270:
      self.setheading(90)
    
  def down(self):
    if self.heading() != 90:
      self.setheading(-90)

  def left(self):
    if self.heading() != 0:
      self.setheading(180)

  def right(self):
    if self.heading() != 180:
      self.setheading(0)

  def move(self):
    time.sleep(.25)
    self.fd(20)
    if self.xcor() < -240:
      self.alive = False
      for i in body:
        i.ht()
    elif self.xcor() > 240:
      self.alive = False
      for i in body:
        i.ht()
    elif self.ycor() > 240:
      self.alive = False
      for i in body:
        i.ht()
    elif self.ycor() < -240:
      self.alive = False
      for i in body:
        i.ht()
    
    
  def die(self):
    self.alive = False
    exit()


class Segment(Turtle):
  def __init__(self, body):
    super().__init__()
    self.ht()
    self.shape("square")
    self.color(generate_color())
    self.pu()
    self.speed(0)
    self.goto(body[-1].xcor(), body[-1].ycor())
    self.st()

  def move(self, other):
    self.goto(other.xcor(), other.ycor())


class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.pu()
    self.goto(random.randint(-230,230), random.randint(-230,230))
  def relocate(self):
    self.goto(random.randint(-230,230), random.randint(-230,230))


def relocate(self):
  pass

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
playing_area()
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
body = []
player = Head(screen)
apple = Apple()
body.append(player)
a = Segment(body)
a.ht()
body.append(a)
b = Segment(body)
body.append(b)


while player.alive == True:
  player.move()
  if player.distance(apple) < 20:
    apple.relocate()
    body.append(Segment(body))
  for i in range(len(body) - 1, 0, -1):
      body[i].move(body[i-1])
  for i in body:
    for i2 in body:
      if body[i].distance(body[i2]) < 20 and i != i2:
        for i3 in body:
          body[i3].ht()
        exit()

screen.exitonclick()