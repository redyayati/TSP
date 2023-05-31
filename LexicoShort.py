# This is a quick algo of Lexicographic Order 

def swap(arr,i,j) : 
    arr[i] , arr[j] = arr[j] , arr[i]
def splitAndReverse(arr , pos) : 
    end = []
    for i in range(len(arr)-pos) : 
        x = arr.pop()
        end.append(x)
    arr.extend(end)

vals = [8,4,3,9,61,21,14]

loop = True
n = 0 
count = 0
while n == 0 : 
        largesti = -1
        for i in range(len(vals)-1) : 
            if vals[i] < vals[i+1] : 
                largesti = i 
        if largesti == -1 : 
            print("finished")
            n = 1
        if n ==0 : 
            largestj = 0 
            for j in range(len(vals)) : 
                if vals[largesti] < vals[j] : largestj = j
            swap(vals, largesti , largestj)
            splitAndReverse(vals, largesti+1)
            # print(vals)
        count += 1
print(count)