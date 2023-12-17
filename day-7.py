## Day 7: Camel Cards ##

from collections import Counter, OrderedDict

# This function will label the hand strength
def find_type(hand_labeled):
    # Five of a kind
    if len(hand_labeled) == 1:
        return "Five_of_a_kind"
    
    # Four of a kind OR Full house
    elif len(hand_labeled) == 2:
        for key in hand_labeled:
            if hand_labeled[key] == 4:
                return "Four_of_a_kind"
            elif hand_labeled[key] == 3 or hand_labeled[key] == 2:
                return "Full_house"
            else:
                continue

    # Three of a kind OR Two pair
    elif len(hand_labeled) == 3:
        for key in hand_labeled:
            if hand_labeled[key] == 3:
                return "Three_of_a_kind"
            elif hand_labeled[key] == 2:
                return "Two_pair"
            else:
                continue

    # Pair
    elif len(hand_labeled) == 4:
        return "Pair"
    
    # High Card
    else:
        return "High_card"
    
# Create hand strength dictionaries to separate hands for ranking order
five_of_a_kind_dict = {}
four_of_a_kind_dict = {}
full_house_dict = {}
three_of_a_kind_dict = {}
two_pair_dict = {}
pair_dict = {}
high_card_dict = {}

with open("input.txt", "r") as f:
    for line in f:
        hand, bid = line.strip().split()

        hand_labeled = Counter(hand)
        hand_type = find_type(hand_labeled)
        
        # Add hand to appropriate dictionary based on hand type
        if hand_type == "Five_of_a_kind":
            five_of_a_kind_dict[hand] = bid
        elif hand_type == "Four_of_a_kind":
            four_of_a_kind_dict[hand] = bid
        elif hand_type == "Full_house":
            full_house_dict[hand] = bid
        elif hand_type == "Three_of_a_kind":
            three_of_a_kind_dict[hand] = bid
        elif hand_type == "Two_pair":
            two_pair_dict[hand] = bid
        elif hand_type == "Pair":
            pair_dict[hand] = bid
        else:
            high_card_dict[hand] = bid

    # To order hand strengths based on rules
    ordered_hands = OrderedDict()
    order = "AKQJT98765432"

    # Order hands within its own hand type
    five_of_a_kind_keys = list(five_of_a_kind_dict.keys())
    five_of_a_kind_keys = sorted(five_of_a_kind_keys, key=lambda word: [order.index(c) for c in word])
    
    four_of_a_kind_keys = list(four_of_a_kind_dict.keys())
    four_of_a_kind_keys = sorted(four_of_a_kind_keys, key=lambda word: [order.index(c) for c in word])
  
    full_house_keys = list(full_house_dict.keys())
    full_house_keys = sorted(full_house_keys, key=lambda word: [order.index(c) for c in word])
    
    three_of_a_kind_keys = list(three_of_a_kind_dict.keys())
    three_of_a_kind_keys = sorted(three_of_a_kind_keys, key=lambda word: [order.index(c) for c in word])

    two_pair_keys = list(two_pair_dict.keys())
    two_pair_keys = sorted(two_pair_keys, key=lambda word: [order.index(c) for c in word])

    pair_keys = list(pair_dict.keys())
    pair_keys = sorted(pair_keys, key=lambda word: [order.index(c) for c in word])

    high_card_keys = list(high_card_dict.keys())
    high_card_keys = sorted(high_card_keys, key=lambda word: [order.index(c) for c in word])


    # Converge order hands based on strength
    for key in high_card_keys[::-1]:
        ordered_hands[key] = high_card_dict[key]

    for key in pair_keys[::-1]:
        ordered_hands[key] = pair_dict[key]
    
    for key in two_pair_keys[::-1]:
        ordered_hands[key] = two_pair_dict[key]

    for key in three_of_a_kind_keys[::-1]:
        ordered_hands[key] = three_of_a_kind_dict[key]

    for key in full_house_keys[::-1]:
        ordered_hands[key] = full_house_dict[key]

    for key in four_of_a_kind_keys[::-1]:
        ordered_hands[key] = four_of_a_kind_dict[key]

    for key in five_of_a_kind_keys[::-1]:
        ordered_hands[key] = five_of_a_kind_dict[key]

    # Determine total winnings 
    total_winnings = 0
    for rank, item in enumerate(ordered_hands, start=1):
        total_winnings += (int(ordered_hands[item]) * rank)

    print(total_winnings) 