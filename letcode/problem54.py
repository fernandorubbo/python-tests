class Problem54:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

#      jl     jr
#  it [ 1, 2, 3]
#     [ 4, 5, 6]
#  ib [ 7, 8, 9]

# [[1]]
# [[1,2]]
# [[1,2],[3,4]]
# [[1,2,3],[4,5,6],[7,8,9]]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#         jl  jr
#  /ib [ 1, 2 ]
#  it           j   i

        i = j = 0
        it = jl = 0
        ib = len(matrix)-1
        jr = len(matrix[0])-1
        result = []
        while it <= ib and jl <= jr:
            while j <= jr:
                result.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            it += 1
            if it <= ib:
                while i <= ib:
                    result.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                jr -= 1
                if jl <= jr:
                    while j >= jl:
                        result.append(matrix[i][j])
                        j -= 1
                    j += 1
                    i -= 1
                    ib -= 1
                    if it <= ib:
                        while i >= it:
                            result.append(matrix[i][j])
                            i -= 1
                        i += 1
                        j += 1
                        jl += 1




        return result