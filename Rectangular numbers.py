def printpattern(n):
    arraySize=n*2-1
    result=[[0 for x in range(arraySize)]
               for y in range(arraySize)]
    for i in range(arraySize):
        for j in range(arraySize):
            if (abs(i-(arraySize//2))> abs(j-(arraySize//2))):
                result[i][j]=abs(i-(arraySize//2))+1
            else:
                result[i][j]=abs(j-(arraySize//2))+1
    for i in range(arraySize):
        for j in range(arraySize):
            print(result[i][j],end="")
        print("")
n=int(input())
printpattern(n)
