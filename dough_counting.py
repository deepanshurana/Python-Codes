money = int(input('Enter the money: '))
l = ['2000', '1000', '500', '200', '50', '100', '10']
l2 = [0, 0, 0, 0, 0, 0, 0]
d = dict(zip(l,l2))  # zip(): to convert list of keys and values into dictionary. This works great if the keys have
                    #  different values, for the keys have same values, use dict.fromkeys(list,value)
                    # done in following code afterwards
print(d)
while money != 0:
    if money >= 2000:
        money -= 2000
        d['2000'] += 1
    elif money >= 500:
        money -= 500
        d['500'] += 1
    elif money >= 200:
        money -= 200
        d['200'] += 1
    elif money >= 100:
        money -= 100
        d['100'] += 1
    elif money >= 50:
        money -= 50
        d['50'] += 1
    else:
        money -= 10
        d['10'] += 1
for i in d:
    if d[i] != 0:
        print(i," used by the amount of : ",d[i])

l3 = [1,2,3,4]
new_d = dict.fromkeys(l3,3)
print(new_d)
