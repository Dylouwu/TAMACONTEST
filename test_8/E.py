from collections import Counter

def main():
    S = input().strip()
    n = len(S)

    char_count = Counter(S)
    total_pairs = n * (n - 1) // 2
    same_pairs = sum(count * (count - 1) // 2 for count in char_count.values())
    nb_possibilities = total_pairs - same_pairs + 1

    print(max(nb_possibilities, 1))

if __name__ == "__main__":
    main()
