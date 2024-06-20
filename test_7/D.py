import sys
import networkx as nx

def main():
    N, M = map(int, input().split())
    pairs = []
    for _ in range(M):
        A, B = map(int, input().split())
        pairs.append((A, B))
    
    origin = [node for node in nx.DiGraph(pairs).nodes if nx.DiGraph(pairs).in_degree(node) == 0]
    
    if len(origin) == 1:
        print(origin[0])
    else:
        print(-1)

if __name__ == "__main__":
    main()
