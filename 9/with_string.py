from typing import List

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
    