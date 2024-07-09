"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
  def topological_sort(graph):
    def dfs(node):
      visited[node] = True
      for neighbor, _ in graph[node]:
        if not visited[neighbor]:
          dfs(neighbor)
      topo_order.append(node)
    
    visited = [False] * len(graph)
    topo_order = []
    
    for node in range(len(graph)):
      if not visited[node]:
        dfs(node)
    
    return topo_order[::-1]

  def calculate_longest_path(graph, topo_order):
    distances = [-float('inf')] * len(graph)
    
    for node in topo_order:  
      if distances[node] == -float('inf'):
        distances[node] = 0
      for neighbor, weight in graph[node]:
        distances[neighbor] = max(distances[neighbor], distances[node] + weight)

    return max(distances)

  if not graph:
    return 0

  topo_order = topological_sort(graph)
  return calculate_longest_path(graph, topo_order)

