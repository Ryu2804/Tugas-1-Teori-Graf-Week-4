import graph 

G = graph.create_graph([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
print("Degree of node 1:", graph.get_degree(G, 1))
print("DFS Traversal starting from node 1:", graph.dfs_traversal(G, 4))
print("BFS Traversal starting from node 1:", graph.bfs_traversal(G, 4))
print("Shortest path from node 1 to node 5:", graph.find_shortest_path(G, 1, 5))
graph.visualize_graph(G)