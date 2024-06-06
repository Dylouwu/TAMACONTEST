def main():
    size = int(input())
    A = []
    for i in range(size):
        inside = input()
        if int(inside.split()[0]) == 1:
            A.append(inside.split()[1])
        elif int(inside.split()[0]) == 2:
            print(A[-int(inside.split()[1])])
    
if __name__ == '__main__':
    main()