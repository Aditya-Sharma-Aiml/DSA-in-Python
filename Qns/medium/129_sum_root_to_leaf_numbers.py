class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, path):
            nonlocal res

            if not root:
                return

            if not root.left and not root.right:
                res += path * 10 + root.val
                return 

            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)

        res = 0
        dfs(root, 0)

        return res

        # Time Complexity O(n)
        # Space Complexity O(1)