def bubble_sort(array):
    size = len(array) #5
    for i in range(size): # 0-4
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j+1] = temp

array = [3, 1, 4, 5, 2] 
bubble_sort(array)
print(array)


