def binary_search(lst, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == key:
            return mid + 1
        elif lst[mid] < key:
            left = mid + 1
        elif lst[mid] > key:
            right = mid - 1
    return left 

def insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        pos = binary_search(lst, 0, i-1, key)
        
        lst[pos+1:i+1] = lst[pos:i]
        lst[pos] = key 
    return lst 

print(insertion([1,2,4,7,3,2,9,-1,-2]))

