def main():
    n = int(input())
    total = 0
    for i in range(n):
        total += i+1-(pow(10,(len(str(i+1)))-1)-1)
    print(total%998244353)
    
if __name__ == '__main__':
    main()