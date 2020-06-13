给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next


def main():
    head = cur = ListNode(1)
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = ListNode(3)
    cur = cur.next
    cur.next = ListNode(4)

    def print_all(head: ListNode) -> None:
        while head:
            print(head.val, '->', end='')
            head = head.next

        print('NULL')

    print_all(print_all(head))
    s = Solution()
    res = s.swapPairs(head)
    print_all(res)


if __name__ == "__main__":
    main()
