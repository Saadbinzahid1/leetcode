class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            num = num * 10 + rem
            temp = temp // 10

        if num == x:
            return True

        return False

