def main():
    K = int(input())
    
    K_binary = bin(K)
    
    #replace all the 1s with 2s
    K_binary = K_binary.replace('1', '2')
    
    #REMOVE 0B
    K_binary = K_binary[2:]
    print(K_binary)
    

if __name__ == '__main__':
    main()