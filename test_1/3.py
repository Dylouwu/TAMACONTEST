def main():
    i = int(input())
    list = []
    for j in range(0, i):
        list.append(input())
    #Determine if it is possible to make the grid contain 6 or more consecutive squares painted black aligned either vertically, horizontally, or diagonally.
    #Check horizontally
    for j in range(0, i):
        for k in range(0, i - 5):
            if list[j][k] == list[j][k + 1] == list[j][k + 2] == list[j][k + 3] == list[j][k + 4] == list[j][k + 5]:
                print("YES")
                return
    #Check vertically
    for j in range(0, i - 5):
        for k in range(0, i):
            if list[j][k] == list[j + 1][k] == list[j + 2][k] == list[j + 3][k] == list[j + 4][k] == list[j + 5][k]:
                print("YES")
                return
    #Check diagonally
    for j in range(0, i - 5):
        for k in range(0, i - 5):
            if (list[j][k] == list[j + 1][k + 1] == list[j + 2][k + 2] == list[j + 3][k + 3] == list[j + 4][k + 4] == list[j + 5][k + 5]) or (list[j][k + 5] == list[j + 1][k + 4] == list[j + 2][k + 3] == list[j + 3][k + 2] == list[j + 4][k + 1] == list[j + 5][k]):
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    main()