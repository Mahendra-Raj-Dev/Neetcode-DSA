# Problem: Serialize and Deserialize Binary Tree
# Pattern: tree (DFS / preorder traversal)
# Approach:
# - Serialize using preorder traversal and mark null nodes with a symbol
# - Deserialize by reconstructing the tree using the same traversal order
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(N), for recursion stack and storage of tokens

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node: 
                res.append("*")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        self.idx = 0

        def dfs():
            if tokens[self.idx] == "*":
                self.idx += 1
                return None
            
            node = TreeNode(int(tokens[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()