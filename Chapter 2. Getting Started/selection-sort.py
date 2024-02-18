'''
Selection-sort algorithm
--- pseudocode

Selection-sort (A, n):

    for i=0 to n:
        substitute = A[i]
        for k=i to n:
            minimal_number = min(minimal_number, A[k])

'''
from typing import List

def selection_sort(nums: List):
    for i in range(len(nums)):
        minimal_number = nums[i]
        for k in range(i, len(nums)):
            if nums[k] < minimal_number:
                temp = nums[k]
                nums[k] = minimal_number
                minimal_number = temp
        nums[i] = minimal_number
    return nums

nums = [5,8,3,9,4,1,2]

print(selection_sort(nums))