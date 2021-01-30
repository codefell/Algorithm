class Solution:
    def intToRoman(self, num: int) -> str:
        m = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        ret = []
        i = 0
        while num:
            if m[i][0] > num:
                i += 1
            else:
                n = num // m[i][0]
                num = num % m[i][0]
                ret += [m[i][1]] * n
        return ''.join(ret)

s = Solution()

test = [0, 1, 499, 500, 3, 4, 9, 58, 1994]

for t in test:
    print(t, s.intToRoman(t))
