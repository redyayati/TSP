import pygame as pg 
from pygame.math import Vector2
import random
pg.init()
width = 800
height = 500 
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Travelling Salesman Problem with Lexicographic Algo')
clock = pg.time.Clock() 
running  = True

base_font = pg.font.SysFont('consolas', 20)
textColor = (255,255,255)
def draw(arr,col,t,xOff, yOff) : 
    for i in range(len(arr)) : 
            x1 , y1 = arr[i].x + xOff , arr[i].y + yOff
            pg.draw.circle(screen, (255,255,255), (int(x1),int(y1)), 10,2)
            if i < len(arr) - 1 :  
                x2 , y2 = arr[i+1].x + xOff , arr[i+1].y + yOff
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

# Lexical order algo : 
def splitAndReverse(arr , pos) : # reverses the array from pos value to the end
    end = []
    for i in range(len(arr)-pos) : 
        x = arr.pop()
        end.append(x)
    arr.extend(end)
def nextOrder()  :
    global count
    largesti = -1
    for i in range(len(orderForLexico)-1) : 
        if orderForLexico[i] < orderForLexico[i+1] : 
            largesti = i 
    if largesti == -1 : 
        return
    largestj = 0 
    for j in range(len(orderForLexico)) : 
        if orderForLexico[largesti] < orderForLexico[j] : largestj = j
    swap(orderForLexico, largesti , largestj)
    splitAndReverse(orderForLexico, largesti+1)
    count += 1

def factorial(n) : 
    if n == 1 : return 1
    else : return n*factorial(n-1)

nodeLength = 8
totalPermutations = factorial(nodeLength)
nodes = [0 for _ in range(nodeLength)]
orderForLexico = []
bestOrder = []
for i in range(len(nodes)) : 
    nodes[i] = Vector2(random.randint(100,width-100), random.randint(10,height/2.5))
    orderForLexico.append(i)

count = 1
recordDistanceLexico = calcDistance(nodes)
bestPathForLexico = nodes.copy()
print(totalPermutations)

while running : 
    screen.fill((0,0,0 ))
    newNodes = []
    for ele in orderForLexico : 
        newNodes.append(nodes[ele])
    draw(newNodes,(255,255,255),1, 0 , 250)
    d = calcDistance(newNodes)
    if d < recordDistanceLexico : 
        recordDistanceLexico = d 
        bestPathForLexico = newNodes.copy()
        bestOrder = orderForLexico.copy()
    totalPercentage = round(100 * count/totalPermutations , 2)
    
    draw(bestPathForLexico , (180,0,0), 5, 0 , 0)
    nextOrder()
    text = base_font.render("Completed : " + str(totalPercentage) + " %",True,textColor)
    screen.blit(text,(10,height-30))

    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_q : 
                running = False 
            if event.key == pg.K_r : 
                for i in range(len(nodes)) : 
                    nodes[i] = Vector2(random.randint(100,width-100), random.randint(10,height/2.5))
                    orderForLexico[i] = i
                recordDistanceLexico = calcDistance(nodes)
                bestPathForLexico = nodes.copy()
                count = 0
    pg.display.flip()
    clock.tick()
pg.quit()
