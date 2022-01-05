class Solution:
    def setOnes(self, matrix):
        ls = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    ls.append((i,j))
        
        while len(ls) > 0:
            a1 = ls[0][0]
            b1 = ls[0][1]
            
            for i in range(len(matrix[0])):
                if matrix[a1][i] != 1:
                    matrix[a1][i] = 1
            for j in range(len(matrix)):
                if matrix[j][b1] != 1:
                    matrix[j][b1] = 1
            ls.pop(0)

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol = Solution()
    sol.setOnes(matrix)
    print(matrix)