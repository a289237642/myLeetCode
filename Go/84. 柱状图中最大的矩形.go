/**
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
*/
package main

func largestRectangleArea(heights []int) int {
	var max int
	var stack = make([]int, 0)
	var nums = make([]int, 0)

	nums = append(nums, []int{0}...)
	nums = append(nums, heights...)
	nums = append(nums, []int{0}...)

	for i := 0; i < len(nums); i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] > nums[i] {
			tmp := stack[len(stack)-1]
			stack = stack[0 : len(stack)-1]

			max = Max(max, nums[tmp]*(i-stack[len(stack)-1]-1))
		}

		stack = append(stack, i)
	}

	return max
}

func Max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
