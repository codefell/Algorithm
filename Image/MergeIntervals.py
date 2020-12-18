class Solution:
    def merge(self, intervals):
        ret = []
        intervals.sort()
        if len(intervals) == 0:
            return ret
        ret.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret

test = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]]
]

s = Solution()

for t in test:
    print(s.merge(t))
