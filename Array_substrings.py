from collections import Counter
s = 'abc'
count = 0
res1 = []
for i in range(len(s)):
    for j in range(len(s)+1):
        res1.append(s[i:j])
print(res1)
res2 = []
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        res2.append(s[j:j+i])
    print(res2)
    res2.clear()

