def main():
    S = input()
    T = ""
    
    for _ in range(10**5):
        T += "oxx"
        
    if S in T:
        print("Yes")
    else:
        print("No")

    
if __name__ == "__main__":
    main()