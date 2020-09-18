# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:55:48 2020

@author: Administrator
"""


import turtle
import random
import time


delay = .1


bg = turtle.Screen ()
bg.tittle =("Snake by Ayush Mahaseth")
bg.bgcolor("pink")
bg.setup (width=600, height=600)
bg.tracer(0)


snake = turtle.Turtle()
food = turtle.Turtle()

snake.penup()
food.penup()
food.color('red')
food.shape('circle')
food.goto(0,100)
snake.speed(0)
snake.shape('square')
snake.shapesize(1, 1, 0)
snake.color('black')



snakebody = []
snakebody.append(snake)


def go():
    if snake.heading() == 90:
        y = snake.ycor()
        snake.sety(y+20)

    if snake.heading() == 270:
        y = snake.ycor()
        snake.sety(y-20)

    if snake.heading() == 0:
        x = snake.xcor()
        snake.setx(x+20)

    if snake.heading() == 180:
        x = snake.xcor()
        snake.setx(x-20)



def up ():
    snake.setheading(90)


def down ():
    snake.setheading(270)

def right ():
    snake.setheading(0)

def left ():
    snake.setheading(180)



turtle.listen()

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")


while True:
    bg.update()
    go()


    if snake.distance(food) <20:
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        food.goto(rand_x,rand_y)

        newbody_seg = turtle.Turtle()
        newbody_seg.speed(0)
        newbody_seg.shape('square')
        newbody_seg.color('green')
        newbody_seg.penup()
        snakebody.append(newbody_seg)

    for i in range(len(snakebody)-1,0,-1):
          X = snakebody[i-1].xcor()
          Y = snakebody[i-1].ycor()
          snakebody[i].goto(X,Y)


    if len(snakebody) > 0:
          X = snake.xcor()
          Y  = snake.ycor()
          snakebody[0].goto(X,Y)

    for i in range(len(snakebody)-2):
        if snakebody[1].distance(snakebody[i+2]) < 20:
            exit()






    time.sleep(delay)
turtle.mainloop()
