class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] != val:
                i += 1
                continue
            if nums[j] == val:
                j -= 1
                continue
            nums[i] = nums[j]
            i += 1
            j -= 1
        return i
        
test = [
    ([3, 2, 2, 3], 3),
    ([0,1,2,2,3,0,4,2], 2),
    ([1, 2, 3], 5),
    ([], 5),
    ([2, 2, 2], 2),
]

s = Solution()

for t in test:
    n = s.removeElement(t[0], t[1])
    print(t[0][0:n])
