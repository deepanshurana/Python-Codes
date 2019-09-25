"""
Q: EQUAL STACKS:
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, 
then print the height. The removals must be performed in such a way as to maximize the height.

SOL: get the 3 array and reverse them, create a new array out of an existing array with each element is sum of all the previous elements.
eg: [3,2,1,1,1] -> [1,1,1,2,3] -> [1,2,3,5,8]
    So the 3 new array formed would be [1,2,3,5,8] [2,5,9] [1,5,6,7]
    Result will be the common elements from the all the list.
    (HERE 5)
    (TO FIND THE MAX H. TAKE THE MAX COMMON ELEMENT)
"""
# using sets for finding common elements in list.
def commonElement(a, b, c):
    aSet = set(a)
    bSet = set(b)
    cSet = set(c)
    if(aSet & bSet & cSet):
        l = list(aSet & bSet & cSet)
        e = max(l)
        return ''.join(str(e))
    return 0

# Function to create a cumulative list from existing one. [1,2,3,4] -> [1,3,6,10].

def cumulative(arr):
    l = []
    sum = 0
    for i in arr:
        sum += i
        l.append(sum)
    return l

def equalStacks(h1, h2, h3):
    
    newh1 = cumulative(reversed(h1))
    newh2 = cumulative(reversed(h2))
    newh3 = cumulative(reversed(h3))

    t = commonElement(newh1, newh2, newh3)
    return t 
    
def main():
    a = [3, 2, 1, 1, 1]
    b = [4, 3, 2]
    c = [1, 1, 4, 1]
    t = equalStacks(h1, h2, h3)
    print(t)
if __name__ == "__main__":
    main()

