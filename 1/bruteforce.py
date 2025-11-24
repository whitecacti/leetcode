from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for first in range(len(nums)):
        remainder = nums[first+1:]
        for second in range(len(remainder)):
            if nums[first] + remainder[second] == target:
            # need to add displacement from first loop to the second
                return [first, second+first+1]

if __name__ == "__main__":
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4], 6))