class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.head:
            return -1

        cur = self.head  # index 0
        for i in range(index):
            cur = cur.next
            if not cur:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.addAtHead(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        if index == 0:
            self.addAtHead(val)
            return

        if not self.head:
            return

        prev_node = self.head
        for i in range(index - 1):
            prev_node = prev_node.next
            if not prev_node:
                return
        next_node = prev_node.next

        if not next_node:
            self.addAtTail(val)
        else:
            new_node.next = next_node
            prev_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.head
        for i in range(index - 1):
            prev_node = prev_node.next
            if not prev_node:
                return
        del_node = prev_node.next
        if not del_node:
            return
        prev_node.next = del_node.next

    def __str__(self):
        l = []
        cur = self.head
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        return "->".join(l)


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class HasCycle:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1, p2 = head, head
        while (p1) and (p2):
            p1 = p1.next
            if not p2.next:
                return False
            p2 = p2.next.next
            if p1 is p2:
                return True
        return False


class DetectCycle:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return

        p1, p2 = head, head

        while True:
            if (not p1) or (not p2):
                return
            if not p2.next:
                return
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                break  # first meet

        p3 = head
        while True:
            if p1 is p3:
                return p1
            p1 = p1.next
            p3 = p3.next


class GetIntersectionNode:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (not headA) or not (headB):
            return

        p1, p2 = headA, headB
        max_rev = 2
        cur_rev = 0

        while cur_rev <= max_rev:
            if p1 is p2:
                return p1

            if p1.next:
                p1 = p1.next
            else:
                p1 = headB
                cur_rev += 1

            if p2.next:
                p2 = p2.next
            else:
                p2 = headA
                cur_rev += 1
        return


class RemoveNthFromEnd:
    def removeNthFromEnd(self, head, n):
        if not head:
            return
        i = 0
        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = head, dummy

        while p1:
            if i >= n:
                p2 = p2.next
            p1 = p1.next
            i += 1

        # delete
        prev_node = p2
        next_node = p2.next.next
        prev_node.next = next_node
        return dummy.next


class ReverseList:
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head

        pos = head
        cur_head = head

        while pos.next:
            swap_node = pos.next
            next_swap = pos.next.next
            pos.next = next_swap

            swap_node.next = cur_head
            cur_head = swap_node
        return cur_head


class ReverseList:
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head

        def helper(node):
            if not node.next:
                return node
            p = helper(node.next)
            node.next.next = node
            node.next = None
            return p

        return helper(head)


class ReverseList:
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        prev_node, cur_node, next_node = None, head, head.next
        while cur_node:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            if next_node:
                next_node = next_node.next
            else:
                next_node = None

        return prev_node


class RemoveElements:
    def removeElements(self, head, val):
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        prev_node, cur_node = dummy, head
        while cur_node:
            if cur_node.val == val:
                prev_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        return dummy.next


class OddEvenList:
    def oddEvenList(self, head):
        if not head:
            return
        p1, p2 = ListNode(None), ListNode(None)
        head_p1 = p1
        head_p2 = p2
        cur = head
        while cur and cur.next:
            next_cur = cur.next.next
            p1.next = cur
            p2.next = cur.next
            cur = next_cur
            p1 = p1.next
            p2 = p2.next
        if cur:
            p1.next = cur
            p1 = p1.next
        p2.next = None
        p1.next = head_p2.next
        return head_p1.next


class IsPalindrome:
    def isPalindrome(self, head):
        if not head:
            return False
        rev_head = None
        cur = head
        while cur:
            node = ListNode(cur.val)
            node.next = rev_head
            rev_head = node
            cur = cur.next
        p1, p2 = head, rev_head
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


class IsPalindrome:
    def isPalindrome(self, head):
        if not head:
            return False
        fast = head
        prev_node, cur_node, next_node = None, head, head.next

        while fast and fast.next:
            fast = fast.next.next

            new_next = cur_node.next.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = new_next

        if fast:  # odd number of elements
            p1, p2 = prev_node, cur_node.next
        else:  # even number of elements
            p1, p2 = prev_node, cur_node
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


# Double Linked List
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # print(self)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.addAtHead(val)
        else:
            self.size += 1
            tail = self.tail
            tail.next = new_node
            new_node.prev = tail
            self.tail = new_node
            # print(self)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)

        next_node = self.head
        for i in range(index):
            next_node = next_node.next
        prev_node = next_node.prev

        prev_node.next = new_node
        new_node.next = next_node
        new_node.prev = prev_node
        next_node.prev = new_node
        self.size += 1
        # print(self)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # print("before deleting")
        # print(self)

        if index >= self.size:
            # print('invalid')
            return

        if index == 0:
            # print('deleting at head')
            self.head = self.head.next
            if self.head:
                self.head.prev = None

            if self.size == 0:
                self.tail = None
            self.size -= 1
            # print(self)
            return

        if index == self.size - 1:
            # print('deleting at tail')
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            if self.size == 0:
                self.head = None
            self.size -= 1
            return

        # delete at index
        del_node = self.head
        for i in range(index):
            del_node = del_node.next
        # print(del_node.val)
        prev_node = del_node.prev
        next_node = del_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        # print(self)

    def __str__(self):
        l = []
        cur = self.head
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        return "DL: " + "->".join(l) + "({})".format(self.size)

