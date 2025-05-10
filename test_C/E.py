def main():
    N = int(input())
    sticks = []
    for _ in range(N):
        sticks.append(input())
    
    unique_sticks = set()
    
    for stick in sticks:
        reversed_stick = stick[::-1]
        unique_sticks.add((stick, reversed_stick))

    seen = set()
    for stick, reversed_stick in unique_sticks:
        normalized = tuple(sorted([stick, reversed_stick]))
        seen.add(normalized)
    
    print(len(seen))

if __name__ == "__main__":
    main()
