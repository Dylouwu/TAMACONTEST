import sys
sys.setrecursionlimit(100000)

def blackboardPairs(i, list, total):
    for j in range(0, i):
        if list[j] % 2 != 0:
            print(total)
            sys.exit()
        list[j] = list[j] / 2
    blackboardPairs(i, list, total + 1)

def main():
    i = int(input())
    list = input().split()
    list = [int(x) for x in list]
    blackboardPairs(i, list, 0)

        

if __name__ == "__main__":
    main()