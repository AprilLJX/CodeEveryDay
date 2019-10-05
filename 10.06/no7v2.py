class Solution:
    def reverse(x: int) -> int:
        xstr = str(abs(x))
        rxstr = int(xstr[::-1])
        if x>=0:
            if rxstr>2**31-1:
                return 0
            else:
                return rxstr
        if x<0:
            if rxstr>2**31:
                return 0
            else:
                return -rxstr


    print(reverse(0))
