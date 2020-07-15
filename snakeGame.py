# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:55:48 2020

@author: Administrator
"""


import turtle
import random

while True:
  rand_x = random.randint(-300,300)
  rand_y = random.randint(-300,300)
  if type(rand_x/12) == int and type(rand_y/12) == int:
      break
bg = turtle.Screen ()
bg.tittle = ("Snake by Ayush Mahaseth")
bg.bgcolor("pink")
bg.setup (width=600, height=600)


tom = turtle.Turtle()
tim = turtle.Turtle()
tom.penup()
tim.penup()
tim.color('red')
tim.shape('square')
tim.goto(rand_x,rand_y)
tom.speed(-1)
tom.shape('square')
tom.color('black')
tom.goto(0,0)

i = 0
def loop():
    while i<50:
        tom.forward(12)
        

    i = i+1




def up ():
  tom.setheading(90)

  tom.forward(12)
def down ():
  tom.setheading(270)
  tom.forward(12)

def right ():
  tom.setheading(0)
  tom.forward(12)

def left ():
  tom.setheading(180)
  tom.forward(12)

i = 0

turtle.listen()

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")


turtle.mainloop()
