def main():
    first = input()
    N = int(first.split()[0])
    Q = int(first.split()[1])
    
    second = input()
    result = 0
    N_list : list = [int(x) for x in second.split()]
    for _ in range(Q):
        query = input()
        l = int(query.split()[1])
        r = int(query.split()[2])
        if query.split()[0] == "1":
            for j in range(l, r):
                result = result + N_list[j]
            print(result)
            result = 0
        else:
            N_list[l] += r
        
        
    


if __name__ == "__main__":
    main()