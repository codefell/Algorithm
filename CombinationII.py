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
        # 1 是包含第一组元素，选择 candidates[0]，然后在 candidates[1:] 上继续找 target - candidates[0]，把找到的所有解前面加上 candidates[0]，然后加入到 ret 中
        sub = self._combinationSum(candidates[1:], target - candidates[0])
        ret.extend([candidates[0:1] + c for c in sub])
        # 2 是不选择第一组元素，先找到第二组元素开始的位置 i，然后在 candidates[i:] 上查找 target，然后将找的所有解加入到 ret 中
        i = 1
        while i < len(candidates) and candidates[i] == candidates[i-1]:
            i += 1
        sub = self._combinationSum(candidates[i:], target)
        ret.extend(sub)

        return ret

    def combinationSum2(self, candidates: list, target: int) -> list:
        # 先将输入排序，方便后面优化，例如如果当前选择的元素总和已经大于 target 了，就不用往后选了，因为后面的数更大
        # 排序之后，candidates 是一组一组相同数字组成的列表，例如 [1, 1, 1, 2, 2, 3, 3, 3]
        candidates.sort()
        # 使用给出的输入和 target 递归调用 _combinationSum 求解
        return self._combinationSum(candidates, target)