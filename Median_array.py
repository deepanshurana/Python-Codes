#==== PROGRAM TO CHECK THE ARRAY MEDIAN PRESENCE WITH sum(left) == sum(right)
import sys

def solve(a):
    Total_sum = sum(a)    # to calculate the total sum of list elements 
    left_part = 0
    for i in range(len(a)):
        current_pointer = a[i]  
        Total_sum -= current_pointer   
        if (Total_sum == left_part):
            return 'YES'
        left_part += current_pointer
    return 'NO'
    

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)

#OUTPUT:Input #Testcases	
	#enter the size and then the elements (with space)
	#and get the results
	#eg : 1(only one test case)
	    # 4(size of array)
	    # 5 4 1 9 (here 1 is a point where sum (left) == sum(right)) hence, return True 
	    # value	
