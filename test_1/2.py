def main():
    list = []
    while True:
        inside = int(input())
        list.append(inside)
        if inside == 0:
            break
        
        
    for i in range(len(list) - 1, -1, -1):
        print(list[i]) 
    

if __name__ == "__main__":
    main()
