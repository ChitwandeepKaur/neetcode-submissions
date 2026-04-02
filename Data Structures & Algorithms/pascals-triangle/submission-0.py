class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        res = []
        temp = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            temp = [0, 1, 1, 0]
            j = 0
            k = 1
            res.append([1])
            res.append([1,1])
            for i in range(3, numRows + 1):
                noOfElements = i
                ans = []
                for l in range(0, noOfElements):
                    ans.append(temp[j] + temp[k])
                    j += 1
                    k += 1
                temp = [0, *ans, 0]
                res.append(ans)
                j = 0
                k = 1

        return res
