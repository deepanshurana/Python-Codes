'''for i in range(0, 5):
    for j in range(0, i + 1):
        print("* ", end="")
    print()'''


'''k = 1
for i in range (0, 5):
    for j in range(0, k):
        print ("* ",end="")
    k = k + 2
    print()'''


'''k = 5
for i in range(0, 5):
	for j in range(0, k):
		print(end=" ")
	k = k - 1
	for j in range(0, i+1):
		print("* ", end="")
	print()'''




'''num = 1
for i in range(0, 5):
	num = 1
	for j in range(0, i+1):
		print(num, end=" ")
		num = num + 1
	print()'''
̃̃

'''n = 1
for i in range(0, 5):
    n = 1
    for j in range(0, i+1):
	    print(n, end=" ")
		n = n + 1
	print()'''



num = 1
for i in range(0, 5):
	for j in range(5, i, -1):
		print(num, end=" ")
		num = num + 1
	print()
	num = 1
