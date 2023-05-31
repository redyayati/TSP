import pygame as pg 
pg.init()
width = 800
height = 500
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock() 
running  = True

base_font = pg.font.SysFont('consolas', 50)
textColor = (0,0,0)

def swap(arr,i,j) : 
    arr[i] , arr[j] = arr[j] , arr[i]
def splitAndReverse(arr , pos) : 
    end = []
    for i in range(len(arr)-pos) : 
        x = arr.pop()
        end.append(x)
    arr.extend(end)

vals = [0,1,2,3]
n = 0
loop = True


while running : 
    screen.fill((255,255,255))

    n += 1
    if loop == True :
        largestI = -1
        for i in range(len(vals)-1) : 
            if vals[i] < vals[i+1] : 
                largestI = i 
        if largestI == -1 : 
            loop = False
            print("Done, No. of interations : ", n )
        if loop == True : 
            largestJ = 0
            for j in range(len(vals)) : 
                if vals[largestI] < vals[j] : largestJ = j
            swap(vals , largestI , largestJ)
            splitAndReverse(vals,largestI+1)

    text = base_font.render(str(vals),True,textColor)
    screen.blit(text,(180,200))


    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_q : 
                running = False 
    pg.display.flip()
    clock.tick(30)
pg.quit()
