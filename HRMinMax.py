
newl = [2, 6, 1, 12]
lit = []
res = []
res.append(max(newl))
temp = []
#------------------------------------------------------------
for i in range(2, len(newl)+1):                                         #               |  [2, 6] [6, 1] [1, 12]
    print("WINDOW:", i)                                                      #          |  [2, 6, 1] [6, 1, 12]
    for j in range(len(newl)-i+1):    # code for substring formation with equal length. |  [2, 6, 1, 12]
        temp = list(newl[j:j+i])                    #(starting with length 2)           
#------------------------------------------------------------
        print(temp)           
        lit.append(min(temp))         # for every window find the minimum values.
        print("----")
    print(lit)
    print("Calculating max of lit: ", end=' ') 
    res.append(max(lit))                # Out of loop, and for every windowresult, put the value in resultant.
    lit.clear()
print(res)
