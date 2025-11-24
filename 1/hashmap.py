from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map and hash_map[complement] != i:
            return [i, hash_map[complement]]
        
    return []


if __name__ == "__main__":
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4], 6))