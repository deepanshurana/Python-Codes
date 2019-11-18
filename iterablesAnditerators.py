"""
ITERABLE: A simple representation of series of elements that can be iterated over. has .iter() or __iter__() method. This method invokes the iterator.

ITERATOR: An object with iteration state. Can check multiple elements using next() or __next__() method. 
"""
nums = '123'
# print(next(nums))# gives error; str object 'nums' is not an iterator.
# print(dir(nums)) # gives all the methods used with it.

i_nums = iter(nums)# this is an iterator.
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums)) # this will raise StopIteration exception with an error.
# to prevent error:
while True:
    try:
        print(next(i_nums))
    except StopIteration:
        break

'''------------------------------------------------------------------------'''
""" to use practical approach for iterators and iterables, you can add your own
method in your class and make them iterables."""

"""Create class that works like builtin range function."""

class myRange():
    # create a starting and ending point.
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # now from above we know that for something to be iterable, it must have
    # an __iter__() method.

    def __iter__(self): # this makes the class iterable. 
        return self

    def __next__(self): # this makes the class an iterator.
        if self.value >= self.end:
            raise StopIteration
        currentVal = self.value
        self.value += 1
        return currentVal

print('\n')
print("Making class iterable as well as iterator...\n")

classRange = myRange(1, 10)

print(next(classRange))
print(next(classRange))
print(next(classRange))
print(next(classRange))
