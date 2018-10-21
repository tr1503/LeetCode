#Use traditional dfs(white,gray,black) to check if the node has cycle in the graph
#If this node has cycle with its neighboor node, return false
class Solution:
    def helper(self, graph, curr, color):
        if color[curr] > 0:
            #if this node is gray, it already has a cycle with neighboor nodes
            #if it is black, no cycle, return true
            return color[curr] == 2
        color[curr] = 1
        for node in graph[curr]:
            if color[node] == 2:
                continue
            #if its neighboor is gray or its neighboor becomes gray after dfs recursion
            #it has cycle, return false
            if color[node] == 1 or self.helper(graph,node,color) == False:
                return False
        color[curr] = 2
        return True
    
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        res = []
        color = [0 for _ in range(n)] #0 is white, 1 is gray, 2 is black
        for i in range(n):
            if self.helper(graph,i,color):
                res.append(i)
        return res
