from random import *
from turtle import *
from base import floor , vector


path=Turtle(visible=True)

aim=vector(5,0)
pacman=vector(-40,-80)
speed= 5
ghosts =[[vector(-180,160),vector(speed,0)],[vector(-180,-160),vector(0,speed)],
         [vector(-100,160),vector(0,-speed)],[vector(100,-160),vector(-speed,0)]]
tiles= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,
        0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,
        0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,
        0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,
        0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,
        0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,
        0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,
        0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,
        0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,
        0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,
        0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,
        0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,
        0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,
        0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,
        0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        ]
def square(x,y):
        path.up()
        path.goto(x,y)
        path.down()

        path.begin_fill()
        for count in range (4):
                path.forward(20)
                path.left(90)
        path.end_fill()


def offset(point):
        x=(floor(point.x,20)+200)/20
        y=(180-floor(point.y,20))/20
        #print(x,y)
        index=int(x+y*20)
        return index




def valid(point):
        index=offset(point)

        #checking vertical collision of tiles
        if tiles[index]==0:
            return False
        #checking horizontal collision of tiles
        index = offset(point+19)
        if tiles[index]==0:
            return False
        return point.x % 20 ==0 or point.y % 20 ==0

def move():
        "move pacman and all ghosts"
        clear()
        if valid(pacman+aim):
            pacman.move(aim)
        index = offset(pacman)
        if tiles[index]==1:
            tiles[index]=2
            x=(index % 20)*20-200
            y=180 - (index // 20)*20
            square(x,y)


        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20,'yellow')

        "ghosts or enemies"
        for point, course in ghosts:
                if valid(point+course):
                        point.move(course)
                else:
                        options=[vector(speed,0),
                                 vector(-speed,0),
                                 vector(0,speed),
                                 vector(0,-speed)]
                        plan = choice(options)
                        course.x =plan.x
                        course.y =plan.y
                up()
                goto(point.x+10 , point.y+10)
                dot(20,'red')

        update()
        for point,course in ghosts:
                if abs(pacman-point)<20:
                        print("---game over---")
                        return
        count=0
        for index in range(len(tiles)):
                tile=tiles[index]
                if tile==2:
                        count=count+1
                        if count==161:
                                print("you win")
                                return
        print("your score is:",count)

        ontimer(move,75)


def world():
        bgcolor('black')
        path.color('blue')
        blue_tile_count=0

        for index in range(len(tiles)):
                tile=tiles[index]
                if tile>0:
                        #print(tile)
                        x= (index%20)*20-200
                        y=180- (index//20)*20
                        #print(x,y)
                        square(x,y)
                        if tile==1:
                                blue_tile_count+=1
                                path.up()
                                path.goto(x+10,y+10)
                                path.dot(4,'white')
        print(blue_tile_count)

def change(x,y):
        if valid(pacman + vector(x,y)):
            aim.x=x
            aim.y=y



setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
#event handling
onkey(lambda : change(speed,0),'Right')
onkey(lambda : change(-speed,0),'Left')
onkey(lambda : change(0,speed),'Up')
onkey(lambda : change(0,-speed),'Down')
world()
move()
done()




