from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left <= right:
        leftL = s[left]
        rightL = s[right]
        s[left] = rightL
        s[right] = leftL
        left+=1
        right-=1

    return s

print(reverseString(['o','n','e','s']))