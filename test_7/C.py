def main():
    N, D = map(int, input().split())
    S = []

    for _ in range(N):
        S.append(input())
        
    consecutive = 0
    
    for i in range(D):
        for j in range(i, D):
            free = True
            for k in range(N):
                if 'x' in S[k][i:j+1]:
                    free = False
                    break
            if free:
                consecutive = max(consecutive, j - i + 1)
    
    print(consecutive)

if __name__ == "__main__":
    main()
