# Comparing GA and Lexico, side by side 

import pygame as pg 
from pygame.math import Vector2
import random
pg.init()
width = 800 
height = 700 
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Compariing Genetic Algo with Lexico')
clock = pg.time.Clock() 
running  = True

base_font = pg.font.SysFont('consolas', 20)
textColor = (255,255,255)

def draw(arr,col,t,xOff, yOff) : # For drawing the connected lines of the nodes 
    for i in range(len(arr)) : 
            x1 , y1 = int(arr[i].x + xOff) , int(arr[i].y + yOff)
            pg.draw.circle(screen, (255,255,255), (x1,y1), 7,2)
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
def calcDistance(nodes , order) : 
    sum = 0
    newNode = []
    for i in order : 
        newNode.append(nodes[i])
    for i in range(len(nodes)-1) : 
        sum += distance(newNode[i] , newNode[i+1])
    return sum 

# For Lexico : 
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
def calcDistanceLex(nodes) : 
    sum = 0
    for i in range(len(nodes)-1) : 
        sum += distance(nodes[i] , nodes[i+1])
    return sum 


orderForGA = []
# Creating and filling the nodes array, This array consists of random vectors that will be used as coordinates. 
nodeLength = 7
nodes = [0 for _ in range(nodeLength)] 
for i in range(len(nodes)) : 
    nodes[i] = Vector2(random.randint(100,width/2 -100), random.randint(10,height/2.5))
    orderForGA.append(i)
count = 1
totalPermutations = factorial(nodeLength)
recordDistanceLexico = calcDistanceLex(nodes)
bestPathForLexico = nodes.copy()
# print(totalPermutations)
orderForLexico = orderForGA.copy() # Lexico Algo will start with the same order as GA



# Code for GA : 
bestEver = []
currentBest = []
population = []
maxPop = 10
fitness = [0 for _ in range(maxPop)] # Contains the fitnesses of corresponding order elements in population array 
recordDistance = float('inf') # initializing record distance as infinity to start with 
for i in range(maxPop) : # populating the population array by shuffling the order array and storing each variationg in population
    pop = orderForGA.copy()
    random.shuffle(pop)
    population.append(pop)
def calculateFitness() : 
    global recordDistance
    global bestEver, gen , bestGen
    global population
    global currentBest
    currentRecord = float('inf')
    for i in range(len(population)) : 
        d = calcDistance(nodes , population[i])
        if d < recordDistance : 
            recordDistance = d 
            bestEver = population[i]
            bestGen = gen
        if d < currentRecord : 
            currentRecord = d 
            currentBest = population[i]
        fitness[i] = 1 / (d +1) # The fitness function is reciprocal of total distance. 1 is added to avoid calculation error
def normalizeFitness(): # Normalizing all fitness values by dividing them by total sum of all fitness values
    global fitness
    sum = 0
    for i in range(len(fitness)) : sum += fitness[i] 
    for i in range(len(fitness)) : fitness[i] = fitness[i] / sum 
def nextGeneration(): 
    global population
    newPopulation = []
    for pop in population : 
        orderA = pickOne(population, fitness)
        orderB = pickOne(population, fitness)
        childOrder = crossOver(orderA , orderB)
        mutate(childOrder, 0.01) 
        newPopulation.append(childOrder)
    population = newPopulation
def pickOne(list,probs) : # This is to pick elements from an array based on its corresponding probability value in "probs" array 
    index = 0
    r = random.random()
    while r > 0 : 
        r = r - probs[index]
        index += 1 
    index -= 1 
    return list[index].copy()
def crossOver(orderA, orderB) : 
    start = random.randint(0 , len(orderA)-1)
    end = random.randint(start+1 , len(orderA))
    newOrder = orderA[start : end]
    for index in orderB : 
        if index not in newOrder : 
            newOrder.append(index)
    return newOrder
def mutate(order , mutationRate) : 
    for node in nodes : 
        if random.random() < mutationRate :
            indexA = random.randint(0,len(order)-1)
            indexB = random.randint(0,len(order)-1)
            swap(order, indexA, indexB)


bestGen =0 
gen = 0

while running : 
    screen.fill((50,50,50 ))

    # Steps for GA : 
    calculateFitness()
    normalizeFitness()
    nextGeneration()
    gen+=1
    # Drawing best Ever path 
    bestPathForGA = []
    for i in bestEver : 
        bestPathForGA.append(nodes[i])
    draw(bestPathForGA , (180,0,0), 5, 0 , 0 + 50)

    # Drawing best in the current generation
    current = []
    for i in currentBest : 
        current.append(nodes[i])
    draw(current , (180,180,180), 2, 0 , 320 + 50)

    # Loop for Lexico 
    newNodes = []
    for ele in orderForLexico : 
        newNodes.append(nodes[ele])
    draw(newNodes,(255,255,255),1, 400 , 320 + 50)
    d = calcDistanceLex(newNodes)
    if d < recordDistanceLexico : 
        recordDistanceLexico = d 
        bestPathForLexico = newNodes.copy()
        bestOrder = orderForLexico.copy()
    totalPercentage = round(100 * count/totalPermutations , 2)
    
    draw(bestPathForLexico , (180,0,0), 5, 400 , 0 + 50)
    nextOrder()
    textPopSize = base_font.render("Population Size : " + str(maxPop) + "  Gen : " + str(bestGen) + "  current Gen : "+str(gen),True,textColor)
    screen.blit(textPopSize, (width/2 - 400,height-30))
    textTitle = base_font.render("          GA :                                                                                  Lexico : " ,True,textColor)
    screen.blit(textTitle, (180 , 20))
    textCompleted = base_font.render("Completed : " + str(totalPercentage) + " %",True,textColor)
    screen.blit(textCompleted,(width/2 + 100,height-30))




    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_q : 
                running = False 
            if event.key == pg.K_r :  # Press 'r' to reset and start afresh 
                # For GA
                gen = 0
                for i in range(len(nodes)) : 
                    nodes[i] = Vector2(random.randint(100,width/2 -100), random.randint(10,height/2.5))
                    orderForGA[i] = i
                recordDistance = float('inf')
                bestPathForGA = []
                #For Lexico 
                orderForLexico = orderForGA.copy()
                recordDistanceLexico = calcDistanceLex(nodes)
                bestPathForLexico = nodes.copy()
                count = 1
    pg.display.flip()
    clock.tick()
pg.quit()
