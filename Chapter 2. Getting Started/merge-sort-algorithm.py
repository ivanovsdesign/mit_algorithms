from typing import List

def merge_sort(nums: List) -> List:
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left, right = merge_sort(nums[:middle]), merge_sort(nums[middle:])
    return merge(left,right)

def merge(left, right) -> List:
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


    
nums = [4,2,5,3,9,8,1,2]
middle = len(nums) // 2

print(merge_sort(nums))