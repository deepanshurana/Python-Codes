#=== Program for finding the total targets from pair difference===
import math
import os
import random
import re
import sys


def pairs(k, arr,n):
    return len(set([x + k for x in arr]).intersection(set(arr)))
    
            

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr,n)
    print(result)
