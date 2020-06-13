
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:

# class Solution(object):
#     def detectCycle(self, head):
#         visited = set()

#         node = head
#         while node is not None:
#             if node in visited:
#                 return node
#             else:
#                 visited.add(node)
#                 node = node.next

#         return None

class Solution:
    # @param head, a ListNode
    # @return a list node
    # def detectCycle(self, head):
    #     try:
    #         fast = head.next
    #         slow = head
    #         while fast is not slow:
    #             fast = fast.next.next
    #             slow = slow.next
    #     except:
    #         # if there is an exception, we reach the end and there is no cycle
    #         return None

    #     # since fast starts at head.next, we need to move slow one step forward
    #     slow = slow.next
    #     while head is not slow:
    #         head = head.next
    #         slow = slow.next

    #     return head
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
