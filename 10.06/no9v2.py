class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        if x<0 or (x%10==0 and x!=0):
            return False
        else:
            while  x > y:
                y = y*10 + x%10
               ## print(y)
                x = x//10
        return x==y or x==y//10

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return  str(x) == str(x)[::-1] if x >= 0 else False