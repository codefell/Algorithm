from functools import reduce

# 新的位置 [newX, newY] 和 attempt 是否冲突
def acceptable(attempt, newX, newY):
    for position in attempt:
        # 对于 attempt 中每个放置判断和 [newX, newY] 是否冲突
        inSameColumn = position[0] == newX  # 已放置位置和 newX 同一列
        inDiagonal = abs(position[0] - newX) == abs(position[1] - newY) # 已放置位置和 (newX, newY) 在对角线上
        if inSameColumn or inDiagonal:
            return False
    return True

'''
attempt 是当前尝试的方案, 元素是 [(x0, y0), (x1, y1)]，例如 [(1, 0), (3, 1)] 表示这个尝试在第一行第一列放一个 queen，在第二行第三列放一个 queue
'''

def nqueen(attempt, n):
    solutions = []
    # 如果尝试方案 attempt 的长度等于 n，就是每一行都有可以放置 queen 的位置，说明这是一个可行的解决方案
    # nqueue 返回所有的可行方案，因此返回的是 attempt 的列表，即 [方案一，方案二]
    if len(attempt) == n:
        solutions = [attempt]
    else:
        # 如果 attempt 不够 n，说明当前尝试了前 len(attempt) 行的位置，下面看后面的是否可以在此基础上构成一个可行的解决方案
        for newX in range(n):
            # 在 attempt 下面的一行依次尝试每个位置，新的 queen 位置的水平位置是 newX，垂直位置是 newY = len(attempt)
            newY = len(attempt)
            if acceptable(attempt, newX, newY):
                # 如果新的位置 (newX, newY) 与 attempt 不冲突，则将这个位置放在 attempt 中成为新的 attempt，然后递归调用 nqueue(newAttempt, n)，获得 newAttempt 下所有可行的解决方案
                newAttempt = attempt + [(newX, newY)]
                # 将所有可行方案累加在 solutions
                solutions += nqueen(newAttempt, n)
    return solutions

class Solution:

    def acceptable(self, x, y):
        for position in self.stack:
            # 对于 attempt 中每个放置判断和 [newX, newY] 是否冲突
            inSameColumn = position[0] == x# 已放置位置和 newX 同一列
            inDiagonal = abs(position[0] - x) == abs(position[1] - y) # 已放置位置和 (newX, newY) 在对角线上
            if inSameColumn or inDiagonal:
                return False
        return True
    
    def copyStack(self):
        return [i for i in self.stack]

    def nqueen(self, n):
        if len(self.stack) == n:
            # 当前步骤等于 n，出现一个可行解，加入 self.solutions，复制一下 self.stack，因为后面 self.stack 还要使用
            self.solutions.append(self.copyStack())
        else:
            y = len(self.stack)
            for x in range(n):
                if self.acceptable(x, y):
                    # (x, y) 可用，放到 self.stack 后面并调用 nqueen 继续向下尝试
                    self.stack.append((x, y))
                    self.nqueen(n)
                    # 向下尝试完成，弹出 (x, y)，换 (x + 1, y) 继续尝试
                    self.stack.pop()
        
    def solveNQueens(self, n):
        # 保存所有可行解
        self.solutions = []
        # 保存当前已尝试的方案 [(x0, y0), (x1, y1), ...]
        self.stack = []
        self.nqueen(n)
        # solution 的结构是 [[[1, 0], [3, 1], [0, 2], [2, 3]], [[2, 0], [0, 1], [3, 2], [1, 3]]]
        # 下面的将这个结构格式化为 [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] 这个的输出
        answer = []
        for s in self.solutions:
            ret = [['.'] * n for i in range(n)]
            for i in s:
                ret[i[1]][i[0]] = 'Q'
            answer.append(list(''.join(r) for r in ret))
        return answer

s = Solution()

print(s.solveNQueens(4))
