from timeit import timeit
import collections
import datetime

print(collections.Counter(["hey", "hey"]))
print(collections.Counter(["hey", "hey"])["hey"])




def solution(A):
    # write your code in Python 3.6
    count = collections.Counter(A)
        
        # find the index
    for idx, ch in enumerate(A):
        if count[ch] == 1:
            return idx     
    return -1


print('Solution')
print(solution( [1, 4, 3, 3, 1, 2] ))












xs = [i for i in range(0,10)]
for x in xs:
    pass
    #print(x)
#    xs.pop(0)
          


#xs2 = xs[:]

#xs.remove(4)




def f():
    while len(xs) != 0:
        x = xs.pop()
        print(x)
        print(xs)

#print(timeit("[i for i in range(0,100)]"))
#f()


dict = { "a" : "b" }
#print(dict["de"])
#print(dict["a"])

if "deded" in dict:
    print('ok dope')
else:
    print('nope')

dict1 = {}
print(dict1)

last = 1000000

def fff():
    while len(xs) != 0:
        x = xs.pop()
        print(x)
        return x

fff()

theRange = [i for i in range(0, last)] 
# #A
# # build list upfront
print('A')
start1 = datetime.datetime.now()
while theRange != []:
    theRange.pop()
end1 = datetime.datetime.now()
print(end1 - start1)    




arrUF = [None for i in range(0,last)]
# for i in range(0, last):
#     arrUF[i] = i
# end1 = datetime.datetime.now()
# print(end1 - start1)


# theRange2 = [i for i in range(0,last)]

# start2 = datetime.datetime.now()
# while theRange2 != []:
#     theRange2.pop(0)
# # arr2 = [] 
# # for i in range(0,last):
# #     arr2 
# end2 = datetime.datetime.now()
# print(end2 - start2)

# #B
# # iteratively append a list


last = 1000000

theRange3 = [i for i in range(0,last)]


 


x = 0 
print('B')
xss = []
start3 = datetime.datetime.now()
while theRange3 != []:
    xss.append(theRange3.pop())
import copy





t = int(input())

for z in range(t):
    input()
    realList = [int(n) for n in input().split()]
    sortedList = copy.copy(realList)
    sortedList.sort()
    listLen = len(sortedList)
    for i in range(listLen - 2):
        if realList[i] == sortedList[i]:
            continue
        myInd = realList.index(sortedList[i])
        while myInd > i:
            if myInd == listLen - 1:
                temp = realList[myInd - 2]
                realList[myInd - 2] = realList[myInd - 1]
                realList[myInd - 1] = realList[myInd]
                realList[myInd] = temp
            else:
                temp = realList[myInd - 1]
                realList[myInd - 1] = realList[myInd]
                realList[myInd] = realList[myInd + 1]
                realList[myInd + 1] = temp
            myInd -= 1
    if realList[listLen - 1] == sortedList[listLen - 1]:
        print("YES")
    else:
        print("NO")
    
# while theRange3 != []:
#     x+= theRange3.pop()
#     def f():
#         print('hey')
#theRange3.reverse() 
# theRange3.reverse()
# while theRange3 != []:
#     theRange3.pop()
# arr2 = [] 
# for i in range(0,last):
#     arr2 
end3 = datetime.datetime.now()
print(end3 - start3)

def isEqual(x,y):
    return x == y















# leaderboard = []

# while xs != []:
#     x = xs.pop()
#     if x not in leaderboard:
#         leaderboard.append(x)

    
