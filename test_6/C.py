def main():
    N = int(input())
    #Print all triples of non-negative integers (x,y,z) such that x+y+z≤N in ascending lexicographical order.
    for x in range(N+1):
        for y in range(N-x+1):
            for z in range(N-x-y+1):
                if x+y+z <= N:
                    print(x,y,z)
    
    
    
if __name__ == "__main__":
    main()
    
    
