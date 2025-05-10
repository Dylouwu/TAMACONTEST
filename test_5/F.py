def main():
    N = int(input())
    S = input()
    K = 0
    
    result = ""
    
    for i in range(N):
        if S[i] == '"':
            K += 1
            result += '"'
        elif S[i] == "," and K % 2 == 0:
            result += "."
        else:
            result += S[i]
            
    print(result)
    
    

if __name__ == '__main__':
    main()