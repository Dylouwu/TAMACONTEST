def smallest_sum(N, M, A):
    cards_on_table = set()
    cards_in_hand = set(A)
    remaining_sum = sum(A)

    for i in range(N):
        # Choose a card from hand to put on the table
        card_chosen = min(cards_in_hand)
        cards_on_table.add(card_chosen)
        cards_in_hand.remove(card_chosen)
        remaining_sum -= card_chosen

        # Keep choosing cards according to the rules
        while True:
            if (card_chosen + 1) % M in cards_in_hand:
                card_chosen = (card_chosen + 1) % M
            elif (card_chosen - 1) % M in cards_in_hand:
                card_chosen = (card_chosen - 1) % M
            else:
                break
            cards_on_table.add(card_chosen)
            cards_in_hand.remove(card_chosen)
            remaining_sum -= card_chosen

    return remaining_sum

nm = input().split()
N = int(nm[0])
M = int(nm[1])
A = list(map(int, input().split()))

print(smallest_sum(N, M, A))
