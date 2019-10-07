from functools import cmp_to_key  # USING CMP_TO_KEY.(for complexity reduction)
from collections import Counter   # to count the occurance of every elements,
                                  # stores in dictionary.


"""  So the problem is complex if we use simple sorting, because there are two types of sorting,
     the first one is in accordance to the occurance (descending order) while the other sorting
     is based on the character value (ascending order). So, we can use comparator function to implement
     these sortings in one go.
"""


# create a class for most common char to store the values of character occurance. 
class MostCommonChar(): 
    def __init__(self, char, occ):
        self.char = char
        self.occ = occ

    # def __str__(self):
    #     if self.occ == 1:
    #          return '{} occured {} time'.format(self.char, self.occ)
    #     return '{} occured {} times'.format(self.char, self.occ)

    # function to compare two objects.
    # refer to https://docs.oracle.com/javase/7/docs/api/java/util/Comparator.html#compare(T,%20T)

    def comparator(a, b):
        if a.occ > b.occ:
            return -1
        elif a.occ < b.occ:
            return 1
        elif a.occ == b.occ:
            if a.char > b.char:
                return 1
            elif a.char < b.char:
                return -1 
            else:
                return 0


def main():
    s = input("Enter the string: ")
    b = Counter(s)
    res = []
    for i in b:
        # creating new objects using the keys and values as a parameter. This
        # will be used by comparator function.

        newObj = MostCommonChar(i, b[i]) 

        # print(newObj)

        # adding the object in list for their later mapping.
        res.append(newObj)

    # print(res)

    # use comparator function to sort two different objects
    # simultaneously.

    res.sort(key=cmp_to_key(MostCommonChar.comparator))
    printCount = 0
    for i in res:
        print(i.char, i.occ)
        printCount += 1
        if (printCount == 3):
            break
    

if __name__ == '__main__':
    main()
