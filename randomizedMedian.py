import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSelect(array, low, high, k):
    if low <= high:
        pivot_index = partition(array, low, high)

        if pivot_index == k:
            return array[pivot_index]
        elif pivot_index < k:
            return quickSelect(array, pivot_index + 1, high, k)
        else:
            return quickSelect(array, low, pivot_index - 1, k)

def randomizedMedian(array):
    n = len(array)
    if n % 2 == 1:
        return quickSelect(array, 0, n - 1, n // 2)
    else:
        left = quickSelect(array, 0, n - 1, n // 2 - 1)
        right = quickSelect(array, 0, n - 1, n // 2)
        return (left + right) / 2

input = [3,1,4,2,2,7,6,5,9,1]
median = randomizedMedian(input)
print("Median:", median)
