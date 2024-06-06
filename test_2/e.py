from itertools import permutations

def difference(a, b, size_x):
    diff = 0
    for i in range(size_x):
        if a[i] != b[i]:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def almost_equal(size_y, size_x, letters):
    for combi in permutations(letters):
        almost = True
        for i in range(size_y - 1):
            if difference(combi[i], combi[i + 1], size_x) == False:
                almost = False
                break
        if almost == True:
            return "Yes"
    return "No"

def main():
    inside = input()
    size_y = int(inside.split()[0])
    size_x = int(inside.split()[1])
    letters = []
    for i in range(size_y):
        letters.append(input())
    print(almost_equal(size_y, size_x, letters))

if __name__ == '__main__':
    main()
