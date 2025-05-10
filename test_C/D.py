def main():
    
    N = int(input())
    A = list(map(int, input().split()))
    
    while True:
        changed = False
        i = 0
        while i < len(A) - 1:
            if abs(A[i] - A[i + 1]) != 1:
                if A[i] < A[i + 1]:
                    A = A[:i + 1] + list(range(A[i] + 1, A[i + 1])) + A[i + 1:]
                else:
                    A = A[:i + 1] + list(range(A[i] - 1, A[i + 1], -1)) + A[i + 1:]
                changed = True
            i += 1
        if not changed:
            break
    
    print(" ".join(map(str, A)))

if __name__ == "__main__":
    main()
