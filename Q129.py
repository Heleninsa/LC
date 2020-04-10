# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        解法： 广度优先遍历
         广度优先遍历模版：
                1. 初始化bfs数组，把起始点加进去, 初始化层次为0
                2. 循环直到符合条件后跳出：
                    2.1. 开一个新的bfs数组
                    2.2. 遍历所有可以走的方向然后加到bfs
                    2.3. 替换bfs数组
                    2.4. 层次+1
                3. 完事
        """
        if root is None:
            return 0
        # 1. 初始化bfs数组，把起始点加进去, 初始化层次为0
        bfs = [root,]
        result = 0
        # 2. 循环直到符合条件后跳出：
        while len(bfs) > 0:
            # 2.1. 开一个新的bfs数组,可以直接用queue
            next_bfs = []
            for i in bfs:
                # 2.2. 遍历所有可以走的方向然后加到bfs
                # left, right 子树
                if i.left is None and i.right is None:
                    # 说明这是一个叶子结点
                    result += i.val
                    continue
                # 坐方向
                if i.left is not None:
                    # 这个节点的新值 = 父节点 * 10 + 当前节点值
                    left = i.left
                    left.val = i.val * 10 + left.val
                    next_bfs.append(left)
                # 右方向
                if i.right is not None:
                    right = i.right
                    right.val = i.val * 10 + right.val
                    next_bfs.append(right)
            # 2.3. 替换bfs数组
            bfs = next_bfs
        # 3
        return result
