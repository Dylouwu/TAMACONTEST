import random

def main():
    countries = int(input())
    A_input = input().split()
    A = [int(A_input[i]) for i in range(countries)]
    S = []
    T = []
    for _ in range(countries-1):
        read = input().split()
        S.append(int(read[0]))
        T.append(int(read[1]))
    
    for i in range(countries-1):
        if A[i] >= S[i]:
            maxi = A[i] // S[i]
            A[i] -= maxi * S[i]
            A[i+1] += maxi * T[i]
    print(A[countries-1])

if __name__ == '__main__':
    main()
