from typing import Tuple, List
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: List[Tuple[int,int]]) -> nx.Graph:
    G = nx.Graph()
    for u, v in edges:
        G.add_edge(u, v)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> List[int]:
    route = list(nx.dfs_edges(G,start))
    node = [start] + [v for u, v in route]
    return node

def bfs_traversal(G: nx.Graph, start: int) -> List[int]:
    route = list(nx.bfs_edges(G,start))
    node = [start] + [v for u, v in route]
    return node

def find_shortest_path(G: nx.Graph, source: int, target: int) -> List[int]:
    return nx.shortest_path(G, source=source, target=target)
    
def visualize_graph(G: nx.Graph):
    nx.draw(G, with_labels=True)
    plt.show()