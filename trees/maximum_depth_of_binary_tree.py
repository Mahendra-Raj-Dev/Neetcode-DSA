# ********************* Solution 1 *************************
# Problem: Maximum Depth of Binary Tree
# Pattern: tree (DFS)
# Approach:
# - Recursively compute the depth of left and right subtrees
# - Return 1 + maximum of both depths
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], h = 0) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# ************************ Solution 2 ***********************
# Problem: Maximum Depth of Binary Tree
# Pattern: tree (BFS / level-order)
# Approach:
# - Use a queue to perform level-order traversal
# - Increment depth after processing each level
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(W), where W is the maximum width of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1 
        
        return level

# ************************* Solution 3 **********************
# Problem: Maximum Depth of Binary Tree
# Pattern: tree (DFS iterative)
# Approach:
# - Use a stack to store (node, depth)
# - Update maximum depth while traversing
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res