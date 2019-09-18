
newl = [1, 2, 3, 5, 1, 13, 3]
lit = []
res = []
res.append(max(newl))
temp = []
for i in range(2, len(newl)+1):
    print("WINDOW:", i)
    for j in range(len(newl)-i+1):
        temp = list(newl[j:j+i])
        print(temp)
        lit.append(min(temp))
        print("----")
    print(lit)
    print("Calculating max of lit: ", end=' ')
    res.append(max(lit))
    lit.clear()
print(res)
