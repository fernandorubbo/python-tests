class Problem48:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        t = l = 0
        b = r = size-1
        while l<=r:
            for i in range(r-l):
                tmp = matrix[t+i][l]
                matrix[t+i][l] = matrix[b][l+i]
                matrix[b][l+i] = matrix[b-i][r]
                matrix[b-i][r] = matrix[t][r-i]
                matrix[t][r-i] = tmp
            t += 1
            b -= 1
            l += 1
            r -= 1

#           l     r
#       t  [1, 2, 3]
#          [4, 5, 6]
#       b  [7, 8, 9]

#    l            r
# t [5,   1,  9,  11]
#   [2,   4,  8,  10]
#   [13,  3,  6,   7]
# b [15, 14, 12,  16]
