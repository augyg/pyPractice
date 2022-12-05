import random

def solution(S, P, Q):
    # write your code in Python 3.6
    S = [toImpact(i) for i in list(S)] 
    S = safeMkSegTree(S)


    pq = zip(P,Q) 
    results = []
    for q in pq:
        print('ran')
        x = querySegTree(q[0], q[1], S)
        results.append(x)

    
    #optimization : history = []
    #history = []
    for idx, (p, q) in enumerate(pq):

        sliced = S[p:q+1]

        #optim




        o = min(sliced)
        #history.append(o, (p,q+1))

        results.append(o)

    return results

def toImpact(i):
    if i == 'A': return 1
    elif i == 'C': return 2
    elif i == 'G': return 3
    elif i == 'T': return 4
    #else fail


# leaf:

# (idx, None, None)  
    

# odd index:

# (idx, Tree, None) 

# class SegTree:



    

    
class SegsTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None



    def populate(self, array):
        mid = round(len(array) / 2)
        # when non-even, the larger half will be left 
        leftSide = array[0:mid]
        rightSide = array[mid:]

        
        
# what if i said

# Maybe [Int]

# None -> None
# Just [x] -> left = SegTree 


class SegTree:
    def __init__(self, array, lbound, rbound, f, mempty): # could add f and mempty as params
        if len(array) == 1:
            #when lbound + 1 == rbound there is one item
            #:. xs[l] == xs[l:r]
            self.node = array[0]
            self.left = None
            self.right = None
            self.lbound = lbound
            self.rbound = rbound
            self.foldFunc = f
        else: 
            mid = round(len(array) / 2)
            # when non-even, the larger half will be left 
            leftSide = array[0:mid]
            rightSide = array[mid:]
            if leftSide == []:
                self.left = None  
            else:
                self.left = SegTree(leftSide, lbound, (lbound + mid), f, mempty)
            ##############################    
            if rightSide == []:
                self.right = None  
            else:
                self.right = SegTree(rightSide, (lbound + mid), rbound, f, mempty)
            
        # can probably generalize 
            self.lbound = lbound
            self.rbound = rbound
            #self.node = f(self.getLeft(mempty), self.getRight(mempty))
            self.node = f(self.left.node, self.right.node)
            self.foldFunc = f 
    # # both return a number
    # def getLeft(self, mempty):
    #     if type(self.left) == int:
    #         return self.left 
    #     elif self.left == None: 
    #         return mempty # will be mempty 
    #     else:
    #         #is tree
    #         return self.left.node
    # def getRight(self, mempty):
    #     if type(self.right) == int:
    #         return self.right  
    #     elif self.right == None: 
    #         return mempty # will be mempty 
    #     else:
    #         #is tree
    #         return self.right.node



# def querySegTree(lbound, rbound, segT):
#     if lbound < mid: 
#         if rbound < mid: 
#             return querySegTree(lbound, rbound, segT.left)
#         elif rbound > mid: 
#             # we need both sides
#             left = querySegTree(lbound, mid, segT.left)
#             right = querySegTree(mid, rbound, segT.right)
#             return segT.foldFunc(left, right)

#     elif lbound > mid: #then we dont need the right side 
#         if rbound < mid: 
#             raise IndexError
#         elif rbound > mid:
#             return querySegTree(lbound, rbound, segT.right)
#             #we need both sides


def querySegTree(lbound, rbound, segT):
    #check if its a leaf
    #if its not,

    #if the lbound and rbound are the same as the focused tree, then our answer in this recursion, is segT.node
    print('############################################################################')
    #if that ideal case is not true, we must compute the midpoint, and split our query accordingly
    #print(lbound,rbound, segT.lbound, segT.rbound, segT, segT.node)
    
    mid = round((segT.rbound + segT.lbound)/2)
    print((lbound,rbound), (segT.lbound, segT.rbound), mid)
    if lbound == segT.lbound and rbound == segT.rbound:
        return segT.node
    else:
        if lbound < mid: 
            if rbound < mid:
                print('only left')
                print('############################################################################')
                return querySegTree(lbound, rbound, segT.left)
            elif rbound >= mid: 
                # we need both sides
                print('both sides')
                left = querySegTree(lbound, mid, segT.left)
                right = querySegTree(mid, rbound+1, segT.right)
                print('############################################################################')
                return segT.foldFunc(left, right)
            else:
                print('else -> fired #1')                
        elif lbound >= mid: #then we dont need the right side
            print(lbound, 'is greater than', mid)
            if rbound < mid: 
                raise IndexError
            elif rbound > mid:
                print('only right')
                print('############################################################################')
                
                return querySegTree(lbound, rbound, segT.right)
            else:
                print('else -> fired #2')
            #we need both sides

        else:
            print('else -> fired #3')
    
    

def safeMkSegTree(array, f, mempty):
    lbound = 0
    rbound = len(array)
    return SegTree(array, lbound, rbound, f, mempty) 

# segTree = safeMkSegTree([random.randint(0,10) for i in range(0,10)], min, 10000000000)

# print("segTree min", segTree.node)

# segTreeMax = safeMkSegTree([random.randint(0,10) for i in range(0,11)], max, 0)
# print("segTree max", segTreeMax.node)

xs = [1, 5, 10, 8, 8, 8, 5, 8, 7, 1,1]

xsSmall = [1,2,3]

segTreeMin = safeMkSegTree(xs, min, 1000000000000)
#print('seg min try2, said 4 was min:', segTreeMin.node, segTreeMin.node) #.right.node)


print(querySegTree(1,len(xsSmall),segTreeMin))


# someIdx = segTreeMin.<lens>.lbound

# xs[someIdx] = N




# queryRange == treeRange -> node

# queryRange != treeRange -> breakup the slices (until they match a range_) and then compare 
