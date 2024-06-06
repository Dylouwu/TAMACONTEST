def rotate90(S, N):
    S_clockwise = [['' for _ in range(N)] for _ in range(N)]
    S_counterclockwise = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            S_clockwise[j][N - 1 - i] = S[i][j]
            S_counterclockwise[N - 1 - j][i] = S[i][j]
    return S_clockwise, S_counterclockwise
    

def main():
    N = int(input())
    S = [list(input().strip()) for _ in range(N)]
    T = [list(input().strip()) for _ in range(N)]
    S_clockwise, S_counterclockwise = rotate90(S, N)
    
    print(T)
    print("----------------")
    print(S_clockwise)
    print("----------------")
    print(S_counterclockwise)
    if S_clockwise == T or S_counterclockwise == T:
        print('Yes')
        
#add translation
    
if __name__ == '__main__':
    main()