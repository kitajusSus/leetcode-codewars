class Solution:
    def reverse(self, x: int) -> int:
        #Define 32bit range for int
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        #reversed number
        rev_n = 0 
        #determine the sign of x
        if x< 0: 
            sign = -1 
        else:
            sign = 1

        x = abs(x)
        while x!= 0:
            #take out the last digit of x
            last = x%10 
            x//=10
        # I check for overflow before appending the digit
            if (rev_n > INT_MAX // 10) or (rev_n == INT_MAX // 10 and last > 7):
                return 0
            if (rev_n < INT_MIN // 10) or (rev_n == INT_MIN // 10 and last > 8):
                return 0
            rev_n = rev_n *10+last
        return sign * rev_n
