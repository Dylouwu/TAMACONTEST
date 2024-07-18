def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    temp_sum = sum((i + 1) * A[i] for i in range(M))
    highest_sum = temp_sum

    total = sum(A[:M])

    for i in range(M, N):
        temp_sum += A[i] * M - total
        total += A[i] - A[i - M]
        highest_sum = max(highest_sum, temp_sum)
    
    print(highest_sum)

if __name__ == "__main__":
    main()