"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for num in nums:
#             if num==0:
#                 nums.remove(0)
#                 nums.append(0)
#         return nums


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i, count_0 = 0, 0  # 初始化指针和零的个数
        while i < len(nums) - count_0:  # 只要指针还在要查看的区域内
            if nums[i] == 0:  # 如果遇到零
                nums.append(nums.pop(i))  # 把这个零弹出来，并压入数组末尾
                count_0 += 1  # 零的个数+1
            else:  # 遇到的数不是零
                i += 1  # 查看下一个数


class Solution(objec):
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = num[j], num[i]
            i += 1
        return nums