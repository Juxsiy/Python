def selectionSort(array):
    size = len(array) # 5
    for i in range(size): # от 0 до 4
        min = i # 0
        for j in range(i + 1, size): # от 1 до 4
            if array[j] < array[min]:
                min = j
        (array[i], array[min]) = (array[min], array[i])
    # i = 0 -> min = 0 -> для j от 1 до 4 -> 

array = [3, 1, 4, 5, 2] 
selectionSort(array)
print(array)
