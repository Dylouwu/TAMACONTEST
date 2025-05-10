def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    dico = {}
    for i in range(N):
        if a[i] not in dico:
            dico[a[i]] = 1
        else:
            dico[a[i]] += 1
    print(len(dico.values()))
    
if __name__ == '__main__':
    main()