# The next generation is created without any cross-over. 
# Although, mutation takes place in every new generation. 
# The mutation involved is simple and consists of changing the order by swapping any 2 random elements. 
import pygame as pg 
from pygame.math import Vector2
import random
pg.init()
width = 800
height = 700 
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Travelling Salesperson Problem with Genetic Algo')
clock = pg.time.Clock() 
running  = True

base_font = pg.font.SysFont('consolas', 20)
textColor = (255,255,255)

def draw(arr,col,t, yOff) :  # For drawing the connected lines of the nodes
    for i in range(len(arr)) : 
            x1 , y1 = arr[i].x , arr[i].y + yOff
            pg.draw.circle(screen, "white", (x1,y1), 10,2)
            if i < len(arr) - 1 :  
                x2 , y2 = arr[i+1].x , arr[i+1].y + yOff
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
 
order = []
# Creating and filling the nodes array, This array consists of random vectors that will be used as coordinates. 
nodeLength = 9
nodes = [0 for _ in range(nodeLength)] 
for i in range(len(nodes)) : 
    nodes[i] = Vector2(random.randint(100,width-100), random.randint(10,height/2.5))
    order.append(i)

bestEver = []
currentBest = []
population = []
maxPop = 100
fitness = [0 for _ in range(maxPop)] # Contains the fitnesses of corresponding order elements in population array 
recordDistance = float('inf') # initializing record distance as infinity to start with 

for i in range(maxPop) : # populating the population array by shuffling the order array and storing each variationg in population
    pop = order.copy()
    random.shuffle(pop)
    population.append(pop)

def calculateFitness() : 
    global recordDistance
    global bestEver
    global population
    global currentBest
    currentRecord = float('inf')
    for i in range(len(population)) : 
        d = calcDistance(nodes , population[i])
        if d < recordDistance : 
            recordDistance = d 
            bestEver = population[i]
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
        newOrder = pickOne(population, fitness)
        mutate(newOrder) # Mutaion occures in every Loop 
        newPopulation.append(newOrder)
    population = newPopulation

def pickOne(list,probs) : # This is to pick elements from an array based on its corresponding probability value in "probs" array 
    index = 0
    r = random.random()
    while r > 0 : 
        r = r - probs[index]
        index += 1 
    index -= 1 
    return list[index].copy()

def mutate(order) : 
    indexA = random.randint(0,len(order)-1)
    indexB = random.randint(0,len(order)-1)
    swap(order, indexA, indexB)





while running : 
    screen.fill((0,0,0 ))

    # Steps for GA : 
    calculateFitness()
    normalizeFitness()
    nextGeneration()
    
    # Drawing best Ever path 
    bestPath = []
    for i in bestEver : 
        bestPath.append(nodes[i])
    draw(bestPath , (180,0,0), 5, 0)

    # Drawing best in the current generation
    current = []
    for i in currentBest : 
        current.append(nodes[i])
    draw(current , (180,180,180), 2, 320)
    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_q : 
                running = False 
            if event.key == pg.K_r :  # Press 'r' to reset and start afresh 
                for i in range(len(nodes)) : 
                    nodes[i] = Vector2(random.randint(100,width-100), random.randint(10,height/2.5))
                    order[i] = i
                recordDistance = float('inf')
                bestPath = []
    pg.display.flip()
    clock.tick()
pg.quit()
