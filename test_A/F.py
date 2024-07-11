def main():
    N, M, H, K = map(int, input().split())
    S = input().strip()
    healthpoints = set()
    coordinates = (0, 0)
    
    for _ in range(M):
        healthpoints.add(tuple(map(int, input().split())))

    for s in S:
        if s == "U":
            coordinates = (coordinates[0], coordinates[1] + 1)
        elif s == "D":
            coordinates = (coordinates[0], coordinates[1] - 1)
        elif s == "L":
            coordinates = (coordinates[0] - 1, coordinates[1])
        else:
            coordinates = (coordinates[0] + 1, coordinates[1])
        
        H -= 1
        if H < 0:
            print("No")
            return
        
        if coordinates in healthpoints and H < K:
            H = K
            healthpoints.remove(coordinates)
    
    print("Yes")

if __name__ == "__main__":
    main()
