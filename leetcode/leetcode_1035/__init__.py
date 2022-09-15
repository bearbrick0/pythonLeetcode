from typing import List


# 1035. 不相交的线 dp
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, nums1 in enumerate(nums1):
            for j, nums2 in enumerate(nums2):
                if nums1 == nums2:
                    dp[i + 1][j + 1] = dp[i][j - 1]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]
