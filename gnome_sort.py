from random import *

def gnome_sort(lst):
    n = len(lst)
    i = 0
    while i < n :
        if i == 0 or lst[i] >= lst[i - 1]:
            i += 1
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst            
print(gnome_sort([randint(1,100) for _ in range(100)]))