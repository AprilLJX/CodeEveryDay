class Solution:
    def romanToInt(self, s: str) -> int:
        roma = {'I': 1,  'V': 5,  'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        num = 0
        for i in range(len(s)-1):
            if roma[s[i]]>= roma[s[i+1]]:
                num = num + roma[s[i]]
            else:
                num = num  - roma[s[i]]

        num = num+roma[s[-1]]
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("LVIII"))



