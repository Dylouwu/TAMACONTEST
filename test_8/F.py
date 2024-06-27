def main():
    N = int(input())
    A_dict = {}

    for _ in range(N):
        col = input().split()
        value = int(col[0])
        color = int(col[1])
        
        if color not in A_dict:
            A_dict[color] = []
        A_dict[color].append(value)
        
    max = 0
    for color in A_dict:
        if min(A_dict[color]) > max:
            max = min(A_dict[color])
        
    print(max)

if __name__ == "__main__":
    main()
