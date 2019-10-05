class Solution:
    def reverse( x: int) -> int:
        y , res = abs(x) , 0
        of = (1<<31)-1 if x>0 else (1<<31)
        while y!=0:
            res = y%10 + res*10
            if res > of:
                return 0
            else:
                y = y//10
        return res if x>0 else -res

    print(reverse(123))



