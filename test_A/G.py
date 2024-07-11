import math
def main():

    A, B = map(int, input().split())
    t = A
    i = 0
    g = 1

    while True:
        current = B * i + A / math.sqrt(g)
        if current > t:
            break
        t = current
        g += 1
        i += 1
        if B * i > t: 
            break
        
    print(f"{t:.10f}")

if __name__ == "__main__":
    main()
