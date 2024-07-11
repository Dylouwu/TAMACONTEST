def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

def main():
    N, M = map(int, input().split())
    #find number of unique connected components
    edges = []
    for i in range(M):
        edge = list(map(int, input().split()))
        edges.append(edge)
    
    global graph 
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    global visited
    visited = [False]*(N+1)
    
    
    components = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            components += 1
    
    print(components)

        
        

    
if __name__ == "__main__":
    main()