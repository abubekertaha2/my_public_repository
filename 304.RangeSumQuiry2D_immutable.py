class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rw,cl=len(matrix), len(matrix[0])
        self.prefixSum=[[0]*(cl+1) for _ in range(rw+1)]
        for r in range(rw):
            for c in range(cl):
                left_sub=self.prefixSum[r+1][c]
                top_sub=self.prefixSum[r][c+1]
                additional=self.prefixSum[r][c]
                cur=matrix[r][c]
                self.prefixSum[r+1][c+1]=left_sub + top_sub + cur - additional
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_r1c1=self.prefixSum[row1][col1]
        sum_r1c2=self.prefixSum[row1][col2+1]
        sum_r2c1=self.prefixSum[row2+1][col1]
        sum_r2c2=self.prefixSum[row2+1][col2+1]
        return sum_r1c1 + sum_r2c2 - sum_r1c2 - sum_r2c1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
