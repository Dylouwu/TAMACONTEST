def main():
    K = int(input())
    A, B = map(int, input().split())
    
    A_decimal = int(str(A), K)
    B_decimal = int(str(B), K)
    
    print(A_decimal * B_decimal)
    

if __name__ == '__main__':
    main()