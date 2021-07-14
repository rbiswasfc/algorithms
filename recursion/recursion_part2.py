from typing import List


class MergeSort:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        def merge(l1, l2):
            i, j = 0, 0
            res = []

            while (i < len(l1)) and (j < len(l2)):
                if l1[i] < l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1

            if i < len(l1):
                res.extend(l1[i:])
            if j < len(l2):
                res.extend(l2[j:])
            return res

        N = len(nums)
        divided_set = [[e] for e in nums]

        while len(divided_set) > 1:
            new_set = []
            i = 0
            while i < len(divided_set):
                if i + 1 < len(divided_set):
                    a, b = divided_set[i], divided_set[i + 1]
                    c = merge(a, b)
                    # print(a, b, c)
                    new_set.append(c)
                    i += 2
                else:
                    new_set.append(divided_set[i])
                    i += 1
            divided_set = new_set.copy()

        return divided_set[0]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTDetector:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return

        def helper(node, lb, ub, ptype):
            # print('executing  call with {},{}, {}'.format(lb, ub, ptype))
            if not node:
                return True

            if isinstance(lb, int):
                if node.val <= lb:
                    # print('flagging lb')
                    return False
            if isinstance(ub, int):
                if node.val >= ub:
                    # print('flagging ub')
                    return False

            cond = True
            if node.left:
                cond = cond & (node.val > node.left.val)
            if node.right:
                cond = cond & (node.val < node.right.val)
            if not cond:
                return cond

            if ptype == "root":
                left_ans = helper(node.left, None, node.val, "left")
                if not left_ans:
                    return left_ans

                right_ans = helper(node.right, node.val, None, "right")
                if not right_ans:
                    return right_ans

            if ptype == "left":
                left_ans = helper(node.left, lb, node.val, "left")
                if not left_ans:
                    return left_ans
                right_ans = helper(node.right, node.val, ub, "right")
                if not right_ans:
                    return right_ans

            if ptype == "right":
                left_ans = helper(node.left, lb, node.val, "left")
                if not left_ans:
                    return left_ans
                right_ans = helper(node.right, node.val, ub, "right")
                if not right_ans:
                    return right_ans
            return True

        return helper(root, None, None, "root")

