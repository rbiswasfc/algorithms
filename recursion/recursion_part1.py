from typing import List


class ReverseStringRecursion:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s

        def helper(p1, p2, s):
            if p2 < p1:
                return
            s[p1], s[p2] = s[p2], s[p1]
            helper(p1 + 1, p2 - 1, s)

        helper(0, len(s) - 1, s)


class ReverseStringIteration:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        p1, p2 = 0, len(s) - 1
        while p2 > p1:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodePairLL:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        n0 = head
        n1 = head.next
        n2 = head.next.next

        new_head = n1
        new_head.next = n0
        new_head.next.next = self.swapPairs(n2)

        return new_head


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTTarget:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return

        def helper(node):
            if not node:
                return

            if node.val == val:
                # print('found')
                return node
            # print('not found')
            if node.val > val:
                left_ans = helper(node.left)

                if left_ans:
                    return left_ans
            else:
                right_ans = helper(node.right)
                if right_ans:
                    return right_ans

        return helper(root)


class PascalTriangleII:
    def getRow(self, rowIndex: int) -> List[int]:
        memory = dict()

        def helper(i, j):
            key = "{}_{}".format(i, j)
            if key in memory:
                return memory[key]
            if i == 0:
                return 1
            if (j == i) or (j == 0):
                return 1
            else:
                ans = helper(i - 1, j - 1) + helper(i - 1, j)
                memory[key] = ans
                return ans

        to_return = [0] * (rowIndex + 1)

        for j in range(rowIndex + 1):
            to_return[j] = helper(rowIndex, j)
        return to_return


class PoW:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, a):
            if a == 0:
                return 1
            elif a % 2 == 0:
                return helper(x * x, int(a / 2))
            else:
                return x * helper(x, a - 1)

        if n == 0:
            return 1
        elif n > 0:
            return helper(x, n)
        else:
            r = helper(x, -n)
            return 1.0 / r


class Merge:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(head1, head2, curr):
            if (not head1) and (not head2):
                return

            if not head1:
                curr.next = head2
                return helper(head1, head2.next, curr.next)  # process remaining head2

            if not head2:
                curr.next = head1
                return helper(head1.next, head2, curr.next)  # process remaining head1

            if head1.val > head2.val:
                curr.next = head2
                return helper(head1, head2.next, curr.next)
            else:
                curr.next = head1
                return helper(head1.next, head2, curr.next)

        start = ListNode(0)
        helper(l1, l2, start)
        return start.next
