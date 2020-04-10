# Q542


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        对于每一个元素遍历，其最小距离 = min(top, left, right, down) + 1
        四个方向的最小距离 + 1. 除了0以外以及不存在的方向

        方法1: 直接遍历，对于每个点都广度优先遍历

            广度优先遍历模版：
                1. 初始化bfs数组，把起始点加进去
                2. 循环直到符合条件后跳出：
                    2.1. 开一个新的bfs数组
                    2.2. 遍历所有可以走的方向然后加到bfs
                    2.3. 替换bfs数组
                3. 完事


        方法2：优化，之前的结果可以缓存，广度优先遍历只有当遍历到有更新的才需要继续更新
        '''
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        # dp存各个位置的最小距离
        dp = [[0 for _ in range(col)] for _ in range(row)]
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(row):
            for j in range(col):
                
                # todo: 最简单的版本：每个值都去执行一遍bfs
                # 模版步骤1: 初始化bfs数组，把起始点加进去
                bfs = [(i, j)]
                level = 0
                find = False
                while len(bfs) > 0 and not find:
                    new_bfs = []
                    # 步骤2: 遍历方向
                    for each_point in bfs:
                        if matrix[each_point[0]][each_point[1]] == 0:
                            # 已经找到0了，直接break
                            find = True
                            dp[i][j] = level
                            break
                        for each_direction in offset:
                            next_point = (each_point[0] + each_direction[0], each_point[1] + each_direction[1])
                            # 检查越界
                            if next_point[0] < 0 or next_point[0] >= row or next_point[1] < 0 or next_point[1] >= col:
                                continue
                            new_bfs.append(next_point) 
                    # 步骤3: 更新bfs数组
                    level += 1
                    bfs = new_bfs
        return dp
