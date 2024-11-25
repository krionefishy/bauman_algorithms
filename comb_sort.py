def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True


        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
    
    return arr


print(comb_sort([1,2,3,0,5,4,8,6,7,0]))