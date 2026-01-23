*********************** Solution 1 **************************
# Problem: Count Good Nodes in Binary Tree
# Pattern: tree (DFS)
# Approach:
# - Use DFS while tracking the maximum value along the path
# - Count a node if its value is greater than or equal to the max so far
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node: return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)

************************** Solution 2 ***************************
# Problem: Count Good Nodes in Binary Tree
# Pattern: tree (BFS)
# Approach:
# - Use BFS while carrying the maximum value along the path
# - Count nodes whose value is greater than or equal to the max so far
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(W), where W is the maximum width of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, root.val)])
        res = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                node, maximum = q.popleft()
                if node.val >= maximum:
                    res += 1
                maximum = max(maximum, node.val)
                if node.left: q.append((node.left, maximum))
                if node.right: q.append((node.right, maximum))
        return res
