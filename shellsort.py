from random import *
from time import *
def shell(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap 
            lst[j] = temp
        gap //= 2
    return lst 


print(shell([3,2,4,1,6,7,0,9,15,2,12,15]))