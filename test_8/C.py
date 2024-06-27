import sys

def main():
    A_input = list(map(int, input().split()))
    B_input = list(map(int, input().split()))
    
    for b in B_input:
        if b in A_input:
            A_input.remove(b)
            continue
        print("No")
        sys.exit()  
    
    print("Yes")

    
if __name__ == "__main__":
    main()