print('--'* 50)

list = []   #initialising list
size_of_array = int(input('ENTER THE TOTAL ELEMENTS IN AN ARRAY: ')) #for the total size of an array
for i in range(0,size_of_array):
    value = int(input('Enter the %d element: ' % (i+1)))
    list.append(value)            #appending the list
print('The list is :' , list)
list.sort(reverse=True)       #sorting the list in descending order
difference = list[0]-list[-1]
print ('the max difference in the list is :'  , difference)
print('--'* 50)



