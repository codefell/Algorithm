```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, maxS = 0, float('-inf')
        for i in nums:
            s = max(s + i, i)
            maxS = max(maxS, s)
        return maxS
```

- sum(i) = Max(<span style="color: red">sum(i -1) + nums[i]</span>,  <span style="color: green">nums[i]</span>)，即如果 sum(i - 1) > 0 则算到 sum(i) 里面，否则 sum(i) 就是 nums[i]

    sum[0] = nums[0]

    sum[1] = Max(sum[0] + nums[1], nums[1])

    sum[2] = Max(sum[1] + nums[2], nums[2])

- result = Max(sum[i])
- 可以先在一个循环中求出每个元素 i 的 sum(i)，然后第二个循环中求所有 sum 的 max，也可以在一个循环中完成这两个步骤
- 动态规划的核心在于，i 的解由 i - 1，甚至 i - 2, i - 3, ... 的解得出

