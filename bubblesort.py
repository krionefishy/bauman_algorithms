from random import *
from time import *

def bubblesort(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(0,len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped = True
        if not swapped:
            break
    return lst

lst = [randint(1,10) for i in range(10)]
print(bubblesort(lst))
