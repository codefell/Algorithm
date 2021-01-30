class Solution:

    def maxSubArray(self, nums):
        self.nums = nums

        maxSum = float('-inf')
        for i in range(len(nums)):
            # 和最大的连续子数组必定以数组中的某个元素为结尾
            # 我们不知道是以哪个元素为结尾，因此将以每个元素为结尾的和最大的连续子数组都计算出来，然后比较它们之中那个是最大的
            # self.sum(i) 就是计算以 i 为结尾的和最大的连续子数组
            # 计算 sum(0) sum(1) ... sum(n-1) sum(n) 哪个最大
            if maxSum < self.sum(i):
                maxSum = self.sum(i)
        return maxSum

    def sum(self, i):
        # sum[0] = nums[0]
        if i == 0:
            return self.nums[0]
        else:
            # sum(i) 由 sum(i-1) 计算出来
            if self.sum(i - 1) > 0:
                # 如果 sum(i-1) 为正，sum(i) = sum(i -1) + num[i]
                return self.sum(i-1) + self.nums[i]
            else:
                # 如果 sum(i-1) 为负，sum(i) = num[i]
                return self.nums[i]
