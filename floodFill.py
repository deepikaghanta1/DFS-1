#TC - O(N)
#SC - O(N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        res = image.copy()
        ROWS = len(image)
        COLS = len(image[0])
        visit = set()
        def dfs(r,c,res):
            if r<0 or c<0 or r==ROWS or c == COLS or image[r][c]!=val or (r,c) in visit:
                return 
            res[r][c] = color
            visit.add((r,c))
            dfs(r+1,c,res)
            dfs(r-1,c,res)
            dfs(r,c+1,res)
            dfs(r,c-1,res)
            return res
        return dfs(sr,sc,res)
        