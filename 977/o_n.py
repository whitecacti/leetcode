from typing import List

def sortedSquares(self, nums: List[int]) -> List[int]:
    start = 0
    end = len(nums) - 1
    # pre create an array to be filling with pointers
    array = list(range(end +1))
    while start <= end:
        if nums[start] ** 2 < nums[end] ** 2:
            # -start is necessary to crrect for the left pointer
            array[end-start] = nums[end] ** 2
            end-=1
        else:
            array[end-start] = nums[start] ** 2
            start+=1

    return array

print([-4,-1,0,3,10])
print([-7,-3,2,3,11])