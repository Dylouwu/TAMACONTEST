def main():
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    d = int(numbers[3])
    e = int(numbers[4])
    f = int(numbers[5])
    
    print(((a*b*c) - (d*e*f))%998244353)
    
if __name__ == "__main__":
    main()