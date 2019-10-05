class Solution:
    def myAtoi(self, str: str) -> int:

        str = str.strip()
        print(str)
        signal = 1
        num = 0
        i = 0
        if str.__len__()==0:
            return 0
        if str[0] == '-':
            signal = -1
            i = i+1
        elif str[0] == '+':
            signal = 1
            i = i+1
        while i<str.__len__():
            if str[i].isdigit():
                num = num*10 + int(str[i])
                i = i+1
            else:
                i = str.__len__()
        num = num*signal
        if num > 2**31-1:
            return 2**31 -1
        elif num < -2**31:
            return -2**31
        else:return num

if __name__ == '__main__':
    s = Solution()
    str = "42"
    print(s.myAtoi(str))