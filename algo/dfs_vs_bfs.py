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


# -----------------------

weighted_graph = {
  'A' : [('B', 4), ('G', 1)],  # A -> B (weight 4), A -> G (weight 1)
  'B' : [('C', 3), ('D', 9), ('E', 5), ('G', 1)],
  'C' : [],
  'D' : [],
  'E' : [('F', 2)],
  'F' : [],
  'G' : [('H', 7), ('J',1)],
  'H' : [('I', 6)],
  'I' : [],
  'J' : [('C', 1)]
}

# --- SEARCH --

def bfs_weighted_greedy(graph, start_node, target_node):
    """
    This is a greedy because we are not revisiting nodes
    So, we may not find the best route
    Fast algo.. O(n + edges)
    """
    visited = {start_node}
    queue = [{'node': start_node,
              'route':{
                    'path': [start_node],
                    'depth': 0,
                    'weight': 0}}]
    while queue:
        el = queue.pop(0)
        node = el['node']
        if target_node == node:
            return el['route']

        for neighbor, edge_weight in graph.get(el['node'], []):
            if neighbor not in visited:
                visited.add(neighbor)
                route = el['route']
                queue.append({'node': neighbor,
                              'route':{
                                    'path': route['path'] + [neighbor],
                                    'depth': route['depth'] + 1,
                                    'weight': route['weight'] + edge_weight}})

print("\nBFS GREADY SEARCH A--> C:")
print(bfs_weighted_greedy(weighted_graph, 'A', 'C'))


def bfs_weighted_shortest_route(graph, start_node, target_node):
    """
    BFS to find the shortest path.
    We stop if
     - Total path until the element is bigger than the already found route
     - Total path until the element is bigger than revisiting the same element through another route

    Slower than previus one, but garanteed to get the best answer
    However, complexity is still the same in avg case: O(n + edges), + O(n²) in worst case once we can visit all nodes multiple times
    """
    found = None
    visited = {start_node: 0}         # node, min weight
    queue = [{'node': start_node,
              'route':{
                'path': [start_node],
                'depth': 0,
                'weight': 0}}]
    while queue:
        el = queue.pop(0)
        current_node = el['node']
        current_route = el['route']
        current_weight = current_route['weight']
        if target_node == current_node and \
            (found is None or found['weight'] > current_weight):
                found = el['route']

        current_path = current_route['path']
        current_depth = current_route['depth']
        for neighbor, edge_weight in graph.get(el['node'], []):
            total_weight =  current_weight + edge_weight
            if total_weight >= visited.get(neighbor, float('inf')) or \
                (found is not None and total_weight >= found['weight']):
                continue
            else:
                visited[neighbor] = total_weight

            path = current_path + [neighbor]
            total_depth = current_depth + 1
            queue.append({'node': neighbor,
                          'route':{
                                'path': path,
                                'depth': total_depth,
                                'weight': total_weight}})
    return found


print("BFS SHORTEST ROUTE SEARCH A--> C:")
print(bfs_weighted_shortest_route(weighted_graph, 'A', 'C'))
