from math import floor, log


def main():
    N = int(input())
    byte_num = []
    count = 0
    length = floor(log(N)/log(2))
    for size_bit in range(length, -1, -1):
        if N >= 2**(size_bit):
            byte_num.append(1)
            N -= 2**(size_bit)
        else:
            byte_num.append(0)
    while byte_num[-1] == 0:
        byte_num.pop()
        count += 1
    print(count)
        
        
    
    

if __name__ == '__main__':
    main()