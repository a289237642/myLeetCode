"""
 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
#暴力求解
"""
(1)
for i ->0,n-2
    for j ->i+1,n-1
    (i,j)->最小高度 ，area
    update max=area
(2)
for i->0,n-1
    找到left bound right bound
    area=height[i]*(right-left)
    update max=area
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights=[0]+heights+[0]
        res=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp=stack.pop()
                res=max(res,(i-stack[-1]-1)*heights[tmp])
            stack.append(i)
        return res