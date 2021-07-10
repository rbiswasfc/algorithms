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
