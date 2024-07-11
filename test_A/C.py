def main():
    N = int(input())
    coordinates = [[0, 0]]
    rotate = 0
    directions = list(input())
    for i in range(N):
        if directions[i] == "S":
            if rotate == 0:
                coordinates[0][0] += 1
            elif rotate == 1:
                coordinates[0][1] -= 1
            elif rotate == 2:
                coordinates[0][0] -= 1
            else:
                coordinates[0][1] += 1
        elif directions[i] == "R":
            rotate = (rotate + 1)%4
            
    print(coordinates[0][0], coordinates[0][1])

    
if __name__ == "__main__":
    main()