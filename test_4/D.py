def main():
    firstline = input()
    N = (int(firstline.split()[0]))
    P = (int(firstline.split()[1]))
    a = [int(x) for x in input().split()]
    
    below = 0
    for i in range(N):
        if a[i] < P:
            below += 1
    print(below)
    
if __name__ == '__main__':
    main()