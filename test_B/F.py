def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    occurrences = [[] for _ in range(N + 1)]

    for idx, num in enumerate(A):
        occurrences[num].append(idx)

    f_indices = [(occurrences[i][1], i) for i in range(1, N + 1)]
    
    f_indices.sort()
    
    result = [num for _, num in f_indices]
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
