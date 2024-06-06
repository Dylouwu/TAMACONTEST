import sys


def get_digit(number, n):
    return number // 10**n % 10

def main():
    N = int(input())
    for num in range(10**N-1,10**N):
        for digit in range(N-1, -1, -1):
            if abs(get_digit(num, digit) - (get_digit(num, digit-1))) <= 1:
                if digit == N-2:
                    print(num)
                    sys.exit()
            else:
                break
    
if __name__ == '__main__':
    main()