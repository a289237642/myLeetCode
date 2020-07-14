"""

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        dummy = ListNode(None)
        node = dummy
        ptrs = [head for head in lists]
        ptrs = list(filter(lambda x: x != None, ptrs))
        while ptrs:
            tmp = [node.val for node in ptrs]
            cur = min(tmp)
            min_idx = tmp.index(cur)
            node.next = ptrs[min_idx]
            ptrs[min_idx] = ptrs[min_idx].next
            if not ptrs[min_idx]:
                del ptrs[min_idx]
            node = node.next
        return dummy.next
