import random 

a = [0,1,2,3,4,5,6,7,8]
b = [8,7,6,5,4,3,2,1,0]
def crossOver(orderA, orderB) : 
    start = random.randint(0 , len(orderA)-1)
    print(start)
    end = random.randint(start+1 , len(orderA))
    print(end)
    newOrder = orderA[start : end]
    for index in orderB : 
        if index not in newOrder : 
            newOrder.append(index)
    return newOrder

print(crossOver(a,b))