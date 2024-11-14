from collections import deque



def dfs(graph, node):
    visited = [node]
    stack = deque([node])
    while stack:
        v = stack.pop()
        print(v, end=' ')
        for n in graph[v]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

def dfs_rec(tree, node):
    print(node, end=' ')
    for child in tree[node]:
        dfs_rec(tree, child)


def bfs(graph, node):
    visited = {node}
    fifo = [node]
    while fifo:
        v = fifo.pop(0)
        print(v, end=' ')
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                fifo.append(n)



g = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}
print("DFS: ")
dfs(g, 'A')
print("\nDFS REC: ")
dfs_rec(g, 'A')

print("\nBFS: ")
bfs(g, 'A')
