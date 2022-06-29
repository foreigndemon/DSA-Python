class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0])-1
        direc = 0
        arr = []
        while(t <= b and l <= r):
            if direc == 0:
                for i in range(l,r+1):
                    arr.append(matrix[t][i])
                t += 1
            elif direc == 1:
                for i in range(t, b+1):
                    arr.append(matrix[i][r])
                r -= 1
            elif direc == 2:
                for i in range(r, l-1, -1):
                    arr.append(matrix[b][i])
                b -= 1
            elif direc == 3:
                for i in range(b, t-1, -1):
                    arr.append(matrix[i][l])
                l += 1
            
            direc = (direc+1)%4
        return arr