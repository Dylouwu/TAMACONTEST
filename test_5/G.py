def main():
    N = int(input())
    S = input()
    Q = int(input())#number of operations on S
    for _ in range(Q):
        index = input()
        if index.split()[0] == "1":
            S_list = list(S)
            S_list[int(index.split()[1]) - 1] = index.split()[2]
            S = ''.join(S_list)
        elif index.split()[0] == "2":
            S = S.lower()
        elif index.split()[0] == "3":
            S = S.upper()
    
    print(S)
        
        
    
        
    
    

if __name__ == '__main__':
    main()