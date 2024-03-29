class Solution(object):
    def findSquare(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x, y = 0, 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    t_x = i + 1
                    t_y = y + 1
                    while t_x<n:





print(Solution().findSquare([1, 1, 3]))