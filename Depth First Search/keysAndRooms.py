class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        def dfs(rooms, curr, visited):
            if curr in visited:
                return
            visited.add(curr)
            for key in rooms[curr]:
                dfs(rooms, key, visited)
        dfs(rooms,0,visited)
        return len(visited) == len(rooms)
