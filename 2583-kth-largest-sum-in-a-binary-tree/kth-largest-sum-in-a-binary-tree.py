from collections import deque
from typing import Optional

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        queue = deque([root])
        level_sums = []
        
        # Level-order traversal (BFS)
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)
            
        # Check if we have at least k levels
        if len(level_sums) < k:
            return -1
            
        # Sort in descending order and return the k-th element
        level_sums.sort(reverse=True)
        return level_sums[k - 1]