"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int: 
        dp = [0] * (len(B) + 1)
        res = 0
        for i in range(len(A)):
            for j in range(len(B)-1, -1, -1):
                dp[j+1] = 1 + dp[j] if A[i] == B[j] else 0
            res = max(res, max(dp))
        return res