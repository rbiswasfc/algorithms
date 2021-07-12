from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PreorderTraversal:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        result = []

        def traverse(node):
            result.append(node.val)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(root)
        return result


class InorderTraversal:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)

            result.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(root)
        return result


class PostorderTraversal:
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

            result.append(node.val)

        traverse(root)
        return result


class LevelorderTraversal:
    def levelorder_traversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        result = []
        queue = [[root]]

        while queue:
            nodes = queue.pop(0)
            cur_results = []
            next_nodes = []

            for node in nodes:
                cur_results.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if len(next_nodes) > 0:
                queue.append(next_nodes)
            result.append(cur_results)
        return result


class MaxTreeDepthFinder:
    def get_max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def compute_depth(node, depth, ans):
            if node.left:
                ans = compute_depth(node.left, depth + 1, ans)
            if node.right:
                ans = compute_depth(node.right, depth + 1, ans)

            if depth > ans:
                ans = depth

            return ans

        ans = compute_depth(root, 1, 1)

        return ans


class CheckPathSum:
    def has_path_sum(self, root: TreeNode, targetSum: int) -> bool:
        def check(node, s):
            if not node:
                return False
            s += node.val
            if not node.left and not node.right:
                return s == targetSum
            return check(node.left, s) or check(node.right, s)

        return check(root, 0)
