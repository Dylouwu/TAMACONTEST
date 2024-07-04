from itertools import combinations

def matrix(H, W):
    mat = []
    for _ in range(H):
        mat.append(list(map(int, input().split())))
    return mat

def is_submatrix(A, B, row_indices, col_indices):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if A[row_indices[i]][col_indices[j]] != B[i][j]:
                return False
    return True

def main():
    H1, W1 = map(int, input().split())
    A = matrix(H1, W1)
    H2, W2 = map(int, input().split())
    B = matrix(H2, W2)
    rows = list(combinations(range(H1), H2))
    cols = list(combinations(range(W1), W2))

    for row_indices in rows:
        for col_indices in cols:
            if is_submatrix(A, B, row_indices, col_indices):
                print("Yes")
                return

    print("No")

if __name__ == "__main__":
    main()
