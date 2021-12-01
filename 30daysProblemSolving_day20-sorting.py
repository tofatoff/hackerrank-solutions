#!/bin/python3

import math
import os
import random
import re
import sys


def bubbleSort(arr):
    
    
    numberOfSwaps = 0
    for i in range(len(arr)):
        
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                numberOfSwaps += 1
                
        if numberOfSwaps == 0:
            break
            
    return numberOfSwaps, arr[0], arr[len(arr)-1]


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps, firstElement, lastElement = bubbleSort(a)
    
    print("Array is sorted in",numberOfSwaps,"swaps.")
    print("First Element:",firstElement)
    print("Last Element:",lastElement)
