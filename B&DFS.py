def dfs(visited, graph, node):
    if node not in visited:
        print(node, "-> ", end="")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def bfs(visited, graph, node, queue):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def main():
    visited_dfs = set()
    visited_bfs = []
    queue_bfs = []
    n = int(input("Enter the number of nodes: "))
    graph = dict()
    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        graph[i] = []
        for j in range(1, edges + 1):
            node = int(input("Enter edge {} for node {}: ".format(j, i)))
            graph[i].append(node)

    print("\nDFS Traversal:")
    dfs(visited_dfs, graph, 1)  # Starting DFS from node 1

    print("\n\nBFS Traversal:")
    bfs(visited_bfs, graph, 1, queue_bfs)  # Starting BFS from node 1

main()
