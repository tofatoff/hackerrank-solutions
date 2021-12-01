#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    binary = []
    
    res = n
    
    while res > 0:
        if res % 2 == 0:
            binary.append(0)
        else:
            binary.append(1)
            
        res = int(res/2)
    
    for i in range(int(len(binary)/2)):
        binary[i],binary[len(binary)-1-i] = binary[len(binary)-1-i],binary[i]
    
    count_one_consecutive = 0
    count_one_consecutive_max = 0

    for i in range(len(binary)):
        if binary[i] == 1:
            count_one_consecutive += 1
            
        if count_one_consecutive > count_one_consecutive_max:
            count_one_consecutive_max = count_one_consecutive
            
        if binary[i] == 0:
            count_one_consecutive = 0     
        
    print(count_one_consecutive_max)
    
