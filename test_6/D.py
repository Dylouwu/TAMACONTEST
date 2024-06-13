from math import sqrt

def main():
    N = int(input())
    coords = []
    for _ in range(N):
        coords.append(list(map(int, input().split())))

    max_distance = 0
    for i in range(N):
        for j in range(i + 1, N):
            distance = sqrt((coords[j][0] - coords[i][0])**2 + (coords[j][1] - coords[i][1])**2)
            if distance > max_distance:
                max_distance = distance

    print(max_distance)

if __name__ == "__main__":
    main()
