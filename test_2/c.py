def main():
    a = 0
    b = 3 + a
    c = 1 + b
    d = 4 + c
    e = 1 + d
    f = 5 + e
    g = 9 + f
    
    inside = input()
    p = inside.split()[0]
    q = inside.split()[1]

    if p == 'A':
        p = a
    elif p == 'B':
        p = b
    elif p == 'C':
        p = c
    elif p == 'D':
        p = d
    elif p == 'E':
        p = e
    elif p == 'F':
        p = f
    elif p == 'G':
        p = g
    
    if q == 'A':
        q = a
    elif q == 'B':
        q = b
    elif q == 'C':
        q = c
    elif q == 'D':
        q = d
    elif q == 'E':
        q = e
    elif q == 'F':
        q = f
    elif q == 'G':
        q = g
    
    print(abs(p-q))
    
if __name__ == '__main__':
    main()