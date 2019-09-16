from collections import Counter
s = 'abba'
count = []
c = 0
for i in range(1, len(s)+1):
    res = ["".join(sorted(s[j: j+i])) for j in range(len(s)-i+1)]
    """
        print list of strings of equal length, eg: ['a','b','b','a'] *
         (all the lists are sorted)                ['ab','bb', 'ab'] **
                                                   ['abb', 'abb'] and ['aabb'] *** and ****
        """
    b = Counter(res)  # counter for every iteration in list:
    """ Counter({'a': 2, 'b': 2} -> c  == 1 (1st) -> c == 2(2nd)
        {'ab': 2, 'bb': 1} -> c == 3(1st) -> c == 3(2nd)
        {'abb': 2} -> c == 4(1st)
        {'aabb'} -> c == 4{1st)
        """
    for i in b:
        c += b[i]*(b[i]-1) / 2
    
print(c)
