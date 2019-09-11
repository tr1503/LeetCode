# time is O(n), space is O(n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r > 0:
                    dfs(r-1, c)
                if r + 1 < n:
                    dfs(r+1, c)
                if c > 0:
                    dfs(r, c-1)
                if c + 1 < m:
                    dfs(r, c+1)
        dfs(sr, sc)
        return image
