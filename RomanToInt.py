class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        for i in range(1, len(s)):
            ret += -m[s[i-1]] if m[s[i]] > m[s[i-1]] else m[s[i-1]]
        ret += m[s[-1]]
        return ret

test = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']

s = Solution()

for i in test:
    print(i, s.romanToInt(i))
