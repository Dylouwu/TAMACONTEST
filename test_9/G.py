def main():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    votes = [0] * (N+1)
    for i in range(M):
        votes[A[i]] += 1
        print(votes.index(max(votes)))
        
        
if __name__ == "__main__":
    main()