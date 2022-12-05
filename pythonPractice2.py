import copy 
from datetime import datetime
import random

l = [i for i in range(0,1000000)]
randoms = [random.randint(0,10000) for i in range(0,1000000)]
randomsFML = [1 for i in range(0,100000)] + [2]
print('set')
print(randoms[0:100])
l2 = []

start = datetime.now()
x = 0
for i,j in enumerate(l):
    l[i] = x

    #if randoms.count(i) == 1:
    #    l2.append(i)
    #    break
#     # for (j,j2) in enumerate(l):
#     #     if i == j:
#     #         print('yes')
#     #         break
#     #A : x += i

#     l2.append(i)
# while l != []:
#     l.pop()
#print(x)

end = datetime.now()
print(end - start)
print(x)




 

# with open("input19.txt") as myfile:
#     #head = [next(myfile) for x in range(5)]
#     lines = myfile.read().split('\n')
#     numCases = lines[0]
#     lines2 = lines [1:]
#     print(lines[2])
#     realList = [int(i) for i in lines[2].split()] 
#     sortedList = copy.copy(realList)
#     sortedList.sort()
#     listLen = len(sortedList)
#     for i in range(listLen - 2):
#         if realList[i] == sortedList[i]:
#             continue
#         myInd = realList.index(sortedList[i])
#         while myInd > i:
#             if myInd == listLen - 1:
#                 temp = realList[myInd - 2]
#                 realList[myInd - 2] = realList[myInd - 1]
#                 realList[myInd - 1] = realList[myInd]
#                 realList[myInd] = temp
#             else:
#                 temp = realList[myInd - 1]
#                 realList[myInd - 1] = realList[myInd]
#                 realList[myInd] = realList[myInd + 1]
#                 realList[myInd + 1] = temp
#             myInd -= 1
#     if realList[listLen - 1] == sortedList[listLen - 1]:
#         print("YES")
#     else:
#         print("NO")
    

# import copy

# t = int(input())

# for z in range(t):
#     input()
#     realList = [int(n) for n in input().split()]
#     sortedList = copy.copy(realList)
#     sortedList.sort()
#     listLen = len(sortedList)
#     for i in range(listLen - 2):
#         if realList[i] == sortedList[i]:
#             continue
#         myInd = realList.index(sortedList[i])
#         while myInd > i:
#             if myInd == listLen - 1:
#                 temp = realList[myInd - 2]
#                 realList[myInd - 2] = realList[myInd - 1]
#                 realList[myInd - 1] = realList[myInd]
#                 realList[myInd] = temp
#             else:
#                 temp = realList[myInd - 1]
#                 realList[myInd - 1] = realList[myInd]
#                 realList[myInd] = realList[myInd + 1]
#                 realList[myInd + 1] = temp
#             myInd -= 1
#     if realList[listLen - 1] == sortedList[listLen - 1]:
#         print("YES")
#     else:
#         print("NO")
        

xs = [1,1]

x = 9
while x != 0:
    print('y')
    x = 0
    print('yes')
    
    # x = xs.pop()
    # if x == 1:
    #     x = xs.pop()
    #     print(xs)
    #     print('xs')
    # xs.pop()
    
print(xs)
        
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(N):
#     # write your code in Python 3.6
#     print('got here')
#     n = [int(i) for i in list(format(N, "b"))]

#     print(n)

#     #at last element if len(xs) - 1 == idx 

#     #x <= n[len(n) - counter - 1]

#     longest = 0
#     while n != []:
#         x = n.pop()
#         if x == 0:
#             length = 1
#             counter = 0 
#             while x == 0:
#                 # if there is a next value, assign it as x 
#                 if len(n[0:len(n) - counter - 1]) != 0: 
#                     x = n[len(n) - counter - 1]
#                     length += 1
#                     counter += 1
#                 else: 
#                     n = [] # break out of entire loop
#                     # i think the loop should be done in this case
#                     # in this end of loop, it would have been zeros not wrapped by 1's
#             longest = max(longest, length)
#             n = n[0:len(n) - counter - 1]    
#             #assign new n value based on consumption
#             #longest = max(longest, length)
        
#     return longest

 




# def solution(N):

#     n = [int(i) for i in list(format(N, "b")) ]

#     counter = 0
#     longest = 0
#     #inLoop = False 
#     maybeLoop = False
#     while n != []:
#         x = n.pop() 
#         if x == 1:
            
#             if counter != 0 and maybeLoop:
#                 longest = max(longest, counter)
#                 counter = 0 
#                 maybeLoop = False
#             elif counter == 0:
#                 maybeLoop = True 


#         elif x == 0: # x == 0
#             if maybeLoop == True:
#                 counter += 1 
#         else:
#             print('invalid')
#     return longest
#             # if a 1 comes next this will still be 


# #1 -> not(inLoop)
# #0 -> if inLoop: counter += 1 


# if inLoop and counter != 0 and x == 1:
#     longest = max(longest, counter)


# What is a gap? 

# 1 followed by n zeros followed by 1 
# -> at this second 1, we should check if this gap is the longest 

d = { "a": 1 }
key = "a"



randoms2 = [random.randint(0,10000) for i in range(0,30000)]
r = set(randoms2)
print((list(r) + [-1])[:100])
xs = [i for i in range(0,1000000000)] 

time1 = datetime.now()
 
print(len(xs))
# for i in randoms2:
    
#     try:
#         xs.remove(i)
#     except:
#         print(i)

# print('hey')
# print(len(xs))
    
# for idx, val in enumerate(randoms): 
    
#     if val in d:
#         d[val] = d[val]+1

#     else:
#         d[val] = 0

time2 = datetime.now()
print('y')
print(time2 - time1)


#print(d)
#print(d)



#####CORRECT ANSWER for Frog crosses river
def solution(X, A):
    # write your code in Python 3.6
    #toDelete = [i for i in range(1,X+1)]
    path = {} #dict([(i, False) for i in range(1,X+1)])
    counter = -1 
    A.reverse()
    while (len(path.keys()) != X) and A != []:

        counter += 1 
        x = A.pop()
        path.setdefault(x, True)
        #try: 
        #    toDelete.remove(x)
        #except:
        #    pass

    if len(path.keys()) != X: return -1
    else: return counter
#####################

############################### ANSWER for updating array of indices starting at 0 and either incr. or set to max
def solution(N, A):
    # write your code in Python 3.6
    inDaSea = [0 for i in range(0,N)]
    nPlusOne = len(inDaSea) + 1
    maximum = 0 # we dont actually use this except to virtually set lastMaxSet
                # this just tracks until we do that
    lastMaxSet = 0 
    A.reverse()
    while A != []:
        x = A.pop()
        # x represents the logical Nth , not the index :. idx = x -1 
        if x == nPlusOne:
            #inDaSea = setMax(maximum, inDaSea)
            lastMaxSet = maximum
        elif 0 <= x <= N:
            j = 1 + max(lastMaxSet, inDaSea[x-1])
            inDaSea[x-1] = j
            maximum = max(maximum, j)
        else: 
            pass

    final = [max(i, lastMaxSet) for i in inDaSea]
    # last op will be iterating through once more and saying max(lastMaxSet, thisIdx)
    return final
############################### ANSWER for updating array of indices starting at 0 and either incr. or set to max


### count number of pairs between 0s and 1s further down the list
def solution(A):
    # write your code in Python 3.6
    east = []
    west = []
    for idx, val in enumerate(A):
        if val == 0:
            east.append(idx)
        else:
            west.append(idx)
    numPairs = 0 
    lastIndex_v = len(A) - 1  

    east.reverse()
    while east != []:
        x = east.pop()
        idx = x
        o = lastIndex_v - idx - len(east) 
        numPairs += o


    
    if numPairs > 1000000000: return -1
    else: 
        return numPairs

###################################################################


def plan(history, newQuery):
    newGround = newQuery

    for (result, (lbound,rbound)) in history:
        if (newQuery[0] < lbound) and ((newQuery[1]+1) > rbound):
            #then the past query is contained


            newGround = [(newQuery[0], lbound)]



