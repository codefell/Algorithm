```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
```

- r 的右边总是 >= target：因为 mid >= target 则 r = mid 的左边
- l 的左边总是 < target：因为 mid < target 则 l = mid 的右边
- 循环结束时，必定 r 在 l 的左边，且 r l 满足上面两条性质，则 l 的左边 < target，l 所在位置 >= target，即应该插入的位置
