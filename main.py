from typing import List

# input array 10,20,80,30,60,50, 110,100,130,170
# x = 110
# output 6 element x is present at index 6

# input array 10,20,80,30,60,50, 110,100,130,170
# x = 175
# output x is not present in array.

def linear_search(arr: List[int], target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


test_data: List[int] = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

# print(linear_search(test_data, 5))

def search(arr, curr_index, key):
    if curr_index == -1:
        print('i', curr_index)
        return -1
    if arr[curr_index] == key:
        print('key', key, 'found at index', curr_index)
        return curr_index
    return search(arr, curr_index - 1, key)


# a = search(test_data, len(test_data) -1, 1)
# print(a)


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    swapped = False
     # iterate through the nums
    for i in range(n - 1):
    #  print('i', i)
        for j in range(n - i - 1):
           
            if arr[j] > arr[j + 1]:
                # swap them
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return 
        
         
         
         
         
print(bubble_sort([10, 20, 80, 30]))