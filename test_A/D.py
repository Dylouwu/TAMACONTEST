def main():
    N = int(input())
    P = 0
    board = []
    A = list(map(int, input().split()))
    for i in range(N):
        board.append(0)
        board = [piece + A[i] for piece in board]
    
    for piece in board:
        if piece > 3:
            P += 1
    print(P)

    
if __name__ == "__main__":
    main()