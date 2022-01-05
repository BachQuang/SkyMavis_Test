

class Solution():
    def getProductExceptItSelf(self, array):
        n = len(array)
        leftArr = [1] * n
        leftArr[0] = array[0]
        for i in range(1, n):
            leftArr[i] = leftArr[i-1] * array[i]

        rightCheck = 1
        for i in reversed(range(0, n)):
            if i == 0:
                array[i] = rightCheck
            else:
                temp = rightCheck
                rightCheck *= array[i]
                array[i] = leftArr[i-1] * temp
        return array

if __name__ == "__main__":
    a = [-1,1,0,-3,3]
    sol = Solution()
    print(sol.getProductExceptItSelf(a))