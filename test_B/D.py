def main():
    H, W, N = map(int, input().split())
    grid = [["." for _ in range(W)] for _ in range(H)]  # Create a grid of lists
    coords = (0, 0)
    facing = "N"
    
    for _ in range(N):
        if grid[coords[0]][coords[1]] == ".":
            grid[coords[0]][coords[1]] = "#"
            if facing == "N":
                facing = "E"
            elif facing == "E":
                facing = "S"
            elif facing == "S":
                facing = "W"
            elif facing == "W":
                facing = "N"
        else:
            grid[coords[0]][coords[1]] = "."
            if facing == "N":
                facing = "W"
            elif facing == "E":
                facing = "N"
            elif facing == "S":
                facing = "E"
            elif facing == "W":
                facing = "S"
        
        if facing == "N":
            coords = (coords[0] - 1, coords[1])
        elif facing == "E":
            coords = (coords[0], coords[1] + 1)
        elif facing == "S":
            coords = (coords[0] + 1, coords[1])
        elif facing == "W":
            coords = (coords[0], coords[1] - 1)
        
        coords = ((coords[0] + H) % H, (coords[1] + W) % W)
    
    for i in range(H):
        print("".join(grid[i]))

if __name__ == "__main__":
    main()
