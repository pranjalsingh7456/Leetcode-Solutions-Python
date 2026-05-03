class Solution(object):
    def isPalindrome(self, n1): #121
        n = n1
        def rev (n): #121
            rev = 0
            while n > 0 :#121 >0 
              digit = n%10
              rev = rev*10 + digit
              n = n//10 
            return rev #121
        rev = rev(n1) #121
        if rev == n1:
           return True
        else:
            return False
        
