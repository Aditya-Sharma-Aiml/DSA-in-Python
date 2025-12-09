class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root, is_left):
            nonlocal res

            if not root:
                return

            if not root.left and not root.right and is_left:
                res += root.val

            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, False)

        return res

        # Time Complexity O(n)
        # Space Complexity O(1)