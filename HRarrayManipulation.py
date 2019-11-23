

def arrayManipulation(n, queries):
    res = [0]*(n)
    print(res)
    print(queries)
    for i in range(len(queries)):
        a, b, v = queries[i][0], queries[i][1], queries[i][2]

    # taking O(n*queries); runtime exceeded.    
        # a, b, v = itertools.compress(queries[i], (1, 1, 1))
        # print(a, b, v)
    #     for j in range(a-1,b):
    #         res[j] += v
    #     print(res)
    # return str(max(res))
    
        res[a-1] += v
        if b != len(res):
            res[b] -= v

       #  print(res)
    maxValue = 0
    sumValue = 0
    for i in res:
        sumValue += i
        if sumValue > maxValue:
            maxValue = sumValue
    # maxValue = max(list(itertools.accumulate(res)))
    return str(maxValue)
