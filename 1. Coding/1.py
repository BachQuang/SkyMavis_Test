
def generateMAtrix(m, n):
	matrix = [[0] * n for _ in range(m)]
	count = 1
	for i in range(m):
		for j in range(n):
			matrix[i][j] = count
			count += 1
	return matrix

class Solution:
    def spiralOrder(self, matrix):
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])
        res = []
        for x in range(m * n):
            # print(i, j)
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return res

if __name__ == "__main__":
	m = 6
	n = 6
	matrix = generateMAtrix(6,6)
	sol = Solution()
	res = sol.spiralOrder(matrix)
	print(res)


