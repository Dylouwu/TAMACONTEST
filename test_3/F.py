def main():
    N = int(input())
    output = []

    while N > 0:
        if N % 2 == 0:
            output.append('B')
            N //= 2
        else:
            output.append('A')
            N -= 1

    print(''.join(output[::-1]))

if __name__ == '__main__':
    main()
