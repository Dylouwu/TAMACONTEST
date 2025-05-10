def main():
    N, M = map(int, input().split())
    S = list(input())
    colors = list(map(int, input().split()))
    
    color_indices = [[] for _ in range(M + 1)]
    
    for index, color in enumerate(colors):
        color_indices[color].append(index)
    
    for i in range(1, M + 1):
        indices = color_indices[i]
        if len(indices) > 1:
            last_char = S[indices[-1]]
            for j in reversed(range(1, len(indices))):
                S[indices[j]] = S[indices[j - 1]]
            S[indices[0]] = last_char
    
    print("".join(S))

if __name__ == "__main__":
    main()
