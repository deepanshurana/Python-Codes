def minimumBribes(q):

    res = 0
    swaped = False
    # creating logic whether the situation is good to go or too chaotic.
    for i, j in enumerate(q,0): # enumerate(list, starting index(other than 0))
        # for enumerate(q,3), the indexing will start from 3 rather than 0.
        # 3 1 |                 0 1 |
        # 4 2 |                 1 2 |
        # 5 3 |   originally,   2 5 |
        # 6 5 |                 3 3 |
        # 7 4 |                 4 4 |
        # in this case, the number 5 must not exceed after index 2 value, so we will calculate the difference.
        if (j-1)-i > 2:
            print("Too chaotic")
            return
    # now we have to check the number of bribes count, we can use bubble sort
    for i in range(len(q)-1): # just keep sure that this loop index doesn't get out of bounds.
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                res += 1
                swaped = True
        if swaped:  # so that swaped element doesn't get swapped again.
            swaped = False
        else:
            break  # break after the last element operation has been done!
    print(res)
    return 
