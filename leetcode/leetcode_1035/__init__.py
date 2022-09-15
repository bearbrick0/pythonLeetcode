from typing import List


# 1035. 不相交的线 dp
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(num1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, num1 in enumerate(num1):
            for j, num2 in enumerate(nums2):
                if num1 == nums2:
                    dp[i + 1][j + 1] = dp[i][j - 1]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]
