def factorofA(a, n):
    c = 0
    for i in a:
        if(n % i == 0):
            c += 1
    if (c == len(a)):
        return True
    else:
        return False

def factorofB(b, n):
    c = 0
    for i in b:
        if(i % n == 0):
            c += 1
    if (c == len(b)):
        return True
    else:
        return False

def getTotalX(a, b):
    resultCount = 0
    for i in range(a[-1], b[0]+1):
        if(factorofA(a, i) and factorofB(b, i)):
            resultCount += 1
    return resultCount
