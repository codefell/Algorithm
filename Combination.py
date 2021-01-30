class Solution:
    # _combinationSum 返回解的集合 [[...], [...]]
    def _combinationSum(self, candidates: list, target: int) -> list:
        # 如果 target == 0，就直接找到一个解 []，即不选任何元素
        if target == 0:
            return [[]]
        # 如果 target < 0，没有解，直接返回空，因为 candidates 中都是正数
        if target < 0 or len(candidates) == 0:
            return []
        # ret 存放所有结果
        ret = []
        # 当前的解是两种子问题的和
        # 1 是选择当前元素，即 candidates[0]，然后在 candidates 上继续找 target - candidates[0]，把找到的所有解前面加上 candidates[0] 就是这个子问题的所有解。将它们加入到 ret 中
        sub = self._combinationSum(candidates, target - candidates[0])
        ret.extend([candidates[0:1] + c for c in sub])
        # 2 是不选择当前元素，然后在 candidates[1:] 上查找 target，然后将找的所有解加入到 ret 中
        sub = self._combinationSum(candidates[1:], target)
        ret.extend(sub)

        return ret
        
    def combinationSum(self, candidates: list, target: int) -> list:
        # 先将输入排序，方便后面优化，例如如果当前选择的元素总和已经大于 target 了，就不用往后选了，因为后面的数更大
        candidates.sort()

        # 使用给出的输入和 target 递归调用 _combinationSum 求解
        return self._combinationSum(candidates, target)