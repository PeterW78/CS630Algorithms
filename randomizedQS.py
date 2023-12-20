import random

def randomizedQuickSort(array):
    if (len(array) <= 1):
        return array
    pivot = random.choice(array)
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    equal = [x for x in array if x == pivot ]
    return randomizedQuickSort(left) + equal + randomizedQuickSort(right) 

input = [3,4,6,1,3,7,1,8,3,6,8,2,6]
test = randomizedQuickSort(input)
print(test)