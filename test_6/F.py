def main():
    N = int(input())
    S = input().split()
    T = input().split()
    
    S = [int(s) for s in S]
    T = [int(t) for t in T]
    
    time_1 = T[0] + S[0]
    print(T[0])
    if time_1 > T[1]:
        time_1 = T[1]
    print(time_1)
    for i in range(1, N-1):
        if S[i] + time_1 < T[i]:
            time_1 += S[i]
            print(time_1)
        else:
            time_1 = T[i]
            print(time_1)
        
    
    

if __name__ == "__main__":
    main()