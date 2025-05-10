def main():
    first_line = input().split()
    N = int(first_line[0])
    K = int(first_line[1])
    grades = []
    
    for _ in range(N):
        line = input().split()
        total_score = int(line[0]) + int(line[1]) + int(line[2])
        grades.append(total_score)
    
    grades_sorted = sorted(grades, reverse=True)
    
    kth_highest_score = grades_sorted[K-1]

    for score in grades:
        if score + 300 >= kth_highest_score:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
