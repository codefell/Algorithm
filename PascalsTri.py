class Solution:
    def getRow(self, rowIndex: int) -> list:
        rowIndex += 1
        lastRow = []
        for i in range(rowIndex):
            newRow = [1] * (i + 1)
            for j in range(1, i):
                newRow[j] = lastRow[j - 1] + lastRow[j]
            lastRow = newRow
        return lastRow

s = Solution()

print(s.getRow(33))