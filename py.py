# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


#dict_variable = {key:value for (key,value) in dictonary.items()}
def solution(A, B):
    # write your code in Python 3.8.10
    
    AB = zip(A,B)

    # DETERMINE HOW MANY ARE CONNECTED VIA ODD NUMBER 

    unique = dict(zip([i for i in range(len(A)+1)], [0 for i in range(len(A)+1)]))
    print(unique)
    # NUM CONNECTS DEPENDS ON COUNT FROM LIST FOR EACH 
    # get unique as map then update it 
    for ab in AB:
        left = ab[0]
        right = ab[1]
        unique[left] += 1
        unique[right] += 1

    print(unique)
    count = 0
    for value in unique.values():
        print(value)
        if value % 2 == 0: 
            # even 
            pass
        else:
            count += 1
    
    return count 



{ "" : [to], totalCount ? }
 # or just take len of to 
 # cant double count (Refer to formula)
#


### BUILD A TREE STRATEGY

    # first new connection will always be ++1
    # idx_initial == 1
    # Map 

this must somehow grow out in a clean semi-symmetrical fashion

first step is odd
second step is even
third step is odd  

-- how does 3 relate to 1 ? 

-- on each case, we have to step out, but may or may not multiply the relationships 
-- at each step we can refine the tree \


What is the incremental cause of 7 in no. 2?
    +1 (4->7)
    + 3 because 3 nodes are connected to a node which you are evenly connected to 


The number of possible TO fros multiply(or maybe exponential) as the tree builds

a node has {0,4} connections possible 


{0: 1, 1: 1, 2: 1, 3: 4, 4: 4, 5: 1, 6: 1, 7: 1}

I can definitely use this along with tracking which, to compute the odd cases and then count them up

to:

{ 0: (1,[3])
, 1: (1,[4])
, 2: (1, [3])
, 3: (4, [0,2,4,6])
, 4: (4,[1,3,5,7])
, 5: (1, [4])
, 6: (1, [3])
, 7: (1, [4])
}


{ 0 : [2 odd links , 5 even links ]} <--- step 

anything that the previous index is odd with, the next is even with and vice versa

for example, 3 (with 0,2,6)

3 Odd, 0 Even 

with just 4:

flip(prev) => 0 Odd + 3 Even + 1 Odd -> 1 Odd 3 Even

@1

flip(prev) + 1 odd 

3 Odd, 1 Even + 1 Odd -> 4 Odd, 1 Even 

flip(prev) + 1 odd



(even,odd) :: (Int, Int)

actually i do need to 




{ 0: (1,[3])
, 1: (1,[odd])
, 2: (1, [even])
, 3: (4, [,,4,6])
, 4: (4,[,,,])
, 5: (1, [odd])
, 6: (1, [3])
, 7: (1, [odd])
}

0:
    3 -> ++
    check3 => 0,2,4,6
    check[_self_ ,2,4,6] => 
       2 -> 0 --> nothing
       6 -> 0 --> nothing
       4 -> 0 --> nothing ++ check[_self_, 1, 5 ,7]
                1 -> is odd check so *2 ++ AND nothing 
                5 -> is odd check so *2 ++ AND nothing 
                7 -> is odd check so *2 ++ AND nothing ; since no nodes
                or len() - 1 ; (for self)


to do faster (half time)

when go to lookup, delete self from the looked up item. Then count it twice 

but hold up, we also divide by 2 so /2 *2 -> id 

So just delete from list 
    or removeif 


@ end divide this by 2 

def countConnects(isOddCheck, mappy, idx, count):
    if idx < len(mappy.keys()):
        # do step recurse

        # idx reps key
        thisNodesConnects = mappy[idx] # :: [Int]
        for connection in thisNodesConnects:
            if isOddCheck: 
                count += 1
            else:
                pass
            # connection :: Int 
            countConnects(not(isOddCheck), mappy, connection, count)


        ## 

    else:
        return count
    





# performance of network""" ; UNITS?

# nodes are peer to peer

# PHYSICS
# N links
# N+1 nodes 

# :: Tree , just edges/links are unclear where

# IF ODD -> ++performance


# NOTE: 13000000001 is faster than 2 

# nodePairs = N * (N+1) / 2 where N is number of links

