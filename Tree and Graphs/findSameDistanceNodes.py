import collections
import heapq
def findDestination(edges, source, distance):
  graph = collections.defaultdict(list)
  for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))
  
  heap = [(0, source)]
  visited = {}
  res = []
  while heap:
    d, node = heapq.heappop(heap)
    if node in visited:
      continue 
    visited[node] = d
    for v, w in graph[node]:
      if v not in visited:
        heapq.heappush(heap, (d + w, v))
  for v, w in graph[source]:
    if visited[v] == distance:
      res.append(v)
  return res

def main():
  edges = [[2,1,1],[2,3,1],[3,4,1]]
  source = 2
  distance = 2
  print(findDestination(edges, source, distance))

main()
