class Solution:
    def merge(self, nums1, m, nums2, n):
        i,j = m - 1, n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

test  = [
    [[1,2,3,0,0,0], 3, [4,5,6], 3],
    [[0,0,0], 0, [2,5,6], 3]
]

s = Solution()

for t in test:
    s.merge(t[0], t[1], t[2], t[3])
    print(t[0])

