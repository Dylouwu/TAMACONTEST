def main():
    S = input()
    N = len(S)
    dico = {}
    for char in S:
        if char in dico:
            dico[char] += 1
        else:
            dico[char] = 1
    
    swaps = N*(N-1)//2
    
    repetitions = 0
    for count in dico.values():
        if count > 1:
            repetitions += count*(count-1)//2
    
    permutations = swaps - repetitions
    if permutations == 0:
        permutations = 1
    print(permutations)
    
if __name__ == '__main__':
    main()