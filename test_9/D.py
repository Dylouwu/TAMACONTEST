def main():
    N, M = map(int, input().split())
    
    prices = []
    features = []
    
    for i in range(N):
        product = list(map(int, input().split()))
        prices.append(product[0])
        features.append(set(product[2:]))
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if prices[j] > prices[i]:
                continue
            if features[i].issubset(features[j]):
                if prices[i] > prices[j] or len(features[j]) > len(features[i]):
                    print("Yes")
                    return
    
    print("No")

if __name__ == "__main__":
    main()
