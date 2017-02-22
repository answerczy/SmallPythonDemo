def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i -1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


num = [1,4,55,3,22,54,32,56,34,59]
print(bubbleSort(num))
