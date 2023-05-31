import pygame as pg 
from pygame.math import Vector2
import random
pg.init()
width = 800
height = 500
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock() 
running  = True

def draw(arr,col,t) : 
    for i in range(len(arr)) : 
            x1 , y1 = arr[i].x , arr[i].y
            pg.draw.circle(screen, (255,255,255), (int(x1),int(y1)), 10)
            if i < len(arr) - 1 :  
                x2 , y2 = arr[i+1].x , arr[i+1].y
                pg.draw.line(screen, col, (x1,y1) , (x2,y2) ,t )
def swap(arr,i,j) : 
    arr[i] , arr[j] = arr[j] , arr[i]
def distance(point1,point2) : 
    x1 , y1 = point1.x , point1.y
    x2 , y2 = point2.x , point2.y
    d = (x2 - x1)**2 + (y2-y1)**2
    return d**(1/2) 
def calcDistance(nodes) : 
    sum = 0
    for i in range(len(nodes)-1) : 
        sum += distance(nodes[i] , nodes[i+1])
    return sum 

nodeLength = 6
nodes = [0 for _ in range(nodeLength)]
for i in range(len(nodes)) : 
    nodes[i] = Vector2(random.randint(0,width), random.randint(0,height))

recordDistance = calcDistance(nodes)
bestPath = nodes.copy()

while running : 
    screen.fill((0,0,0 ))
    draw(nodes,(255,255,255),1)
    i = random.randint(0 , len(nodes)-1)
    j = random.randint(0 , len(nodes)-1)
    swap(nodes, i , j)
    d = calcDistance(nodes)
    if d < recordDistance : 
        recordDistance = d 
        bestPath = nodes.copy()
        print(d)
    draw(bestPath , (180,0,0), 5)

    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_q : 
                running = False 
            if event.key == pg.K_r : 
                for i in range(len(nodes)) : 
                    nodes[i] = Vector2(random.randint(0,width), random.randint(0,height))
                recordDistance = calcDistance(nodes)
                bestPath = nodes.copy()
    pg.display.flip()
    clock.tick(60)
pg.quit()
