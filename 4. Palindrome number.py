class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0 :
            return False
        s_x = str(x)
        if s_x == s_x[::-1]:
            return True


#link: https://leetcode.com/problems/palindrome-number/
