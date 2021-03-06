"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""
# 暴力法
class Solution:
    def maxArea(self, height):
        res = 0
        i,j = 0,len(height)-1
        while j > i:
            s = (j-i)*min(height[j],height[i])
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            res = max(res,s)
        return res

# 双指针法
class Solution:
    def maxArea(self, height):
        res = 0
        i,j = 0,len(height)-1
        while j > i:
            s = (j-i)*min(height[j],height[i])
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            res = max(res,s)
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxarea = 0, len(height) - 1, 0
        while left < right:
            maxarea = max(maxarea, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return maxarea