def main():
    i = int(input())
    result_list = []
    data_dict = {}
    for j in range(i):
        inside = input()
        if inside in data_dict:
            data_dict[inside] += 1
            result_list.append(inside + "(" + str(data_dict[inside]) + ")")
        else:
            data_dict[inside] = 0
            result_list.append(inside)
    for j in range(i):
        print(result_list[j])
    
if __name__ == "__main__":
    main()
