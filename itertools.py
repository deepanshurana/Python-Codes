"""
ITERTOOLS: Module which allows us to work with the iterators in a fast and efficient way.
[USED IN FOR LOOP.]
"""


import itertools

# count(). returns an iterator that counts. By default starts with zero.

counter = itertools.count(5, step=-2.5) # step can be -ve, +ve, decimal etc.
# print(dir(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

data = [100, 200, 300, 400, 500]
# zip function works till the termination of shortest iterable.
dailyData = list(zip(itertools.count(), data)) # zip combines two iterables and pairs them correspondingly.
print(dailyData)

# to zip the iterables with longest iterables, use .zip_longest() from itertools.
"""
ZIP_LONGEST: 
WARNING: using zip_longest(), you can't use itertools.count() as it will
run out of memory.

"""
dailyData = list(itertools.zip_longest(range(10), data))
print(dailyData)



"""
CYCLE: takes input like count, and cycles them.

"""
counter = itertools.cycle([1, 2, 3, True, False]) # takes 1 argument, list of anything. 
i = 1
while(i < 7):
    print(next(counter))
    i += 1

"""
Q: print squares of first 10 numbers. 
map() takes the function and iterables uses the iterable values is passed
as an argument.
"""

squares = map(pow, range(1, 10), itertools.repeat(2)) # this is more efficient.
print(list(squares))

squares = list(map(lambda i: i*i, range(1, 10))) # this is less efficient.
print(squares)

"""
STARMAP(): similar to map, but takes a list of tuples as an argument,
and then pairs the tuple elements to each other.
"""
squares = list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 3), (3, 3)]))
print(squares, end='\n\n')


"""COMBINATIONS AND PERMUTATIONS:
Combinations: all different ways you can arrange the certain the items.
(order does not matter)
Permutations: similar to combinations except that order does matter.
"""

letters = ['a', 'b', 'c']
numbers = [0, 1]
names = ['Desmond', 'Miles']
print("Combinations: \n")
res = itertools.combinations(letters, 2)
for i in res:
    print(i)
print("Permutations: \n")
res = itertools.permutations(letters, 2)
for i in res:
    print(i)

# to make repeat of elements, use .product(iterable, repeat=x), x = length of each tuple.
print("Cartesian product.", end='\n\n')
res = itertools.product(numbers, repeat=4)
for i in res:
    print(i)
# to print repeated values in combinations or permutations use _with_replacement().
print("Combinations with replacements(combine with itself.): ", end='\n\n')
res = itertools.combinations_with_replacement(letters, 2)
for i in res:
    print(i)


'''
CHAIN FUNCTION: using multiple iterables.(chaining of iterables.)
'''

# you can create new list and add all the other list, but inefficient.
combine = letters + numbers + names
print("\nNOT USING chain():")
print(combine)
print('\n')
# use chain(i1, i2, i3, ...) for memory efficiency.
print("USING chain():")
combine = list(itertools.chain(letters, numbers, names))
print(combine)
print('\n')



"""
ISLICE(): this method is used for slicing on the iterator.
(memory efficient)
eg: to fetch out some lines from .log files which
contains thousands and thousands of lines.
"""

# BASIC OPERATION:

res = list(itertools.islice(range(10), 5))
print(res)
res = list(itertools.islice(range(10), 1, 5))
print(res)
res = list(itertools.islice(range(10), 1, 5, 2))
print(res)

# ADVANCE OPERATION
# using log file
print("\nUsing islice() to fetch first 3 lines info from log file:\n")
with open('learningitertools.log', 'r') as f:
    info = itertools.islice(f, 3)
    for i in info:
        print(i, end='')


"""
COMPRESS() FUNCTION: (used in Data Science).
selectors will decide the printing outcome of an iterable.
(similar to .filer() function, but in .compress() the selectors are used as
 an iterable.)
"""
testList = [1, 2, 3, 4]
selectors = [True, True, False, True]
print("\n Using .filter():")

def ln(t):
    if t == 3:
        return False
    return True

res = filter(ln, testList)
print(list(res))
print('Using .compress()')
res = itertools.compress(testList, selectors)
print(list(res))
