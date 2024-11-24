from time import *
from random import *
def simple(lst):
    for i in range(len(lst)):
        mn = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[mn]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
    return lst

lst = [randint(1,1000) for i in range(100000)]
start = time()
s = simple(lst)
end = time()
print(abs(start - end))