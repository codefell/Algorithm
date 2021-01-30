class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals):
            if newInterval[0] < intervals[i][0]:
                break
            i += 1
        intervals.insert(i, newInterval)
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret

test  = [
    [[[1,3],[6,9]], [2, 5]],
    [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]],
    [[], [5, 7]],
    [[[1,5]], [2, 3]],
    [[[1,5]], [2, 7]]
]

s = Solution()

for t in test:
    print(s.insert(t[0], t[1]))
