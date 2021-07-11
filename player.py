from random import *
from turtle import *
from base import vector


player=vector(0,0) #where to start
aim= vector(2,0)   #how many steps to move

def wrap (value):
    if value==210:
        dot(10,'red')
    return(value)
def draw():
    #to move player
    player.move(aim)
    player.x=wrap(player.x)
    player.y=wrap(player.y)
    aim.move(random()-0.5)
    aim.rotate(random()*10-1) #1.32*10 ==13 it is used for getting degree

    clear()
    goto(player.x, player.y)
    dot(50,'green')
    if True:
        ontimer(draw,100)





setup(420,620,370,0)
hideturtle()
tracer(False)
up()
draw()
done()