'''
FINDING THE LARGEST RECTANGLE IN A GIVEN HISTOGRAM.
--------------------*OPERATION*-------------------
For every bar, we will calculate the area. For this, we need to know the
index of the first smaller bar (on the left side of currentBar-> X) and index
of the first smaller bar on the right of X. Call them L and R respectively.


We traverse all the bars from left to right. Every bar is pushed to stack once.A bar is popped when a bar of smaller height is seen. Then we calculate the area of popped bar. Increment R + 1 , ( 'i' in this code ). L is the index of previous item (present in stack).

-----------------------*ALGORITHM*------------------
1. Create an Empty stack.

2. Start from first bar, and traverse all the histogram bars.(while i < len).
    a. If stack is empty or h[i] is greater than the bar at the top of stack,
       push the index in stack.

    b. If the current bar h[i] is smaller than top of stack, then keep popping       the index from stack till the bar at the top of stack becomes larger.

3. If stack is not empty, then one by one remove all bars from the step.
   Repeat Step 2.b for every removed bar.
'''

# h -> histogram [list of bars]
h = [1, 2, 3, 4, 5]


def largestRectangle(h):
    stack = []
    area = 0
    maxArea = 0
    i = 0
    while i < len(h):
        if(not stack) or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            # if not stack:
            #     area = i
            # else:
            #     area = h[top]*(i-stack[-1]-1)

            area = (h[top] * ((i - stack[-1] - 1) if stack else i))
            if area > maxArea:
                maxArea = area
    while(stack):
        top = stack.pop()
        # if not stack:
        #     area = i
        # else:
        #     area = h[top]*(i-stack[-1]-1)

        area = (h[top] * ((i - stack[-1] - 1) if stack else i))
        if area > maxArea:
            maxArea = area

    return maxArea


def main():
    histogram = [1, 2, 3, 4, 5]
    res = largestRectangle(histogram)
    print("Largest Rectangle is: ", res)


if __name__ == "__main__":
    main()
