def insertion(lst):
    for i in range(len(lst)):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

print(insertion([1,2,4,7,3,2,9,-1,-2]))