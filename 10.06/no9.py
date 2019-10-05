class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = x
        y = 0
        if x<0:
            return False
        else:
            while x//10 !=0:
                y = y*10 + x%10
               ## print(y)
                x = x//10
        y = y * 10 + x
        if y==x1:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
