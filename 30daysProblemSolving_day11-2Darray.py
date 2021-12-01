#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    summ = arr[0][0]+arr[0][0+1]+arr[0][0+2]+arr[0+1][0+1]+arr[0+2][0]+arr[0+2][0+1]+arr[0+2][0+2]
    summ_max = summ
    
    for i in range(4):
        for j in range(4):
            summ = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if summ > summ_max:
                summ_max = summ
                
    print(summ_max)
