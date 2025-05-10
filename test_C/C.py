def main():
    N = int(input())
    A = list(map(int, input().split()))

    pizza = [0]
    cut = 0
    
    for i in range(N):
        cut = (cut + A[i]) % 360
        pizza.append(cut)
    
    pizza.sort()
    
    max_gap = 0
    for i in range(1, len(pizza)):
        max_gap = max(max_gap, pizza[i] - pizza[i - 1])
    
    max_gap = max(max_gap, 360 - (pizza[-1] - pizza[0]))

    print(max_gap)

if __name__ == "__main__":
    main()
