# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


def main():
    head = cur = ListNode(1)
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = ListNode(3)
    cur = cur.next
    cur.next = ListNode(4)
    cur = cur.next
    cur.next = ListNode(5)

    def print_all(head: ListNode) -> None:
        while head:
            print(head.val, '->', end='')
            head = head.next

        print('NULL')

    print_all(head)
    s = Solution()
    res = s.reverseList(head)
    print_all(res)


if __name__ == "__main__":
    main()
