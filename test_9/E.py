def dfs(ladder, node, visited):# Depth First Search from ChatGPT
    stack = [node]
    max_value = node
    
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        max_value = max(max_value, current)
        if current in ladder:
            for neighbor in ladder[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return max_value

def main():
    N = int(input())
    ladder = dict()
    
    for _ in range(N):
        a, b = map(int, input().split())
        if a not in ladder:
            ladder[a] = []
        if b not in ladder:
            ladder[b] = []
        ladder[a].append(b)
        ladder[b].append(a)
    
    visited = set()
    max_value = dfs(ladder, 1, visited)
    print(max_value)

if __name__ == "__main__":
    main()
