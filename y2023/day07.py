#Task: https://adventofcode.com/2023/day/7
from collections import Counter

f = open('y2023/data/day07.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

RANKS = {
    'five of a kind': 7,
    'four of a kind': 6,
    'full house' : 5,
    'three of a kind': 4,
    'two pair' : 3,
    'one pair' : 2,
    'high card' : 1
}

WEIGHTS = '23456789TJQKA'
ORDER = dict(zip(WEIGHTS, range(len(WEIGHTS))))
WEIGHTS_2 = 'J23456789TQKA'
ORDER_2 = dict(zip(WEIGHTS_2, range(len(WEIGHTS_2))))
JOKER = WEIGHTS_2[0]
ACE = WEIGHTS_2[-1]

def part1():
    hand_ranks = {}
    hand_scores = {}
    for rank in range(1,len(RANKS)+1):
        hand_ranks[rank] = []
        
    for line in lines:
        hand, score = line.split()
        hand_scores[hand]=int(score)
        cards_dict = Counter(hand)
        card_counts = cards_dict.values()

        if 5 in card_counts:
            hand_ranks[RANKS['five of a kind']].append(hand)
        elif 4 in card_counts:
            hand_ranks[RANKS['four of a kind']].append(hand)
        elif 2 in card_counts and 3 in card_counts:
            hand_ranks[RANKS['full house']].append(hand)
        elif 3 in card_counts:
            hand_ranks[RANKS['three of a kind']].append(hand)
        elif Counter(card_counts)[2] == 2:
            hand_ranks[RANKS['two pair']].append(hand)
        elif 2 in card_counts:
            hand_ranks[RANKS['one pair']].append(hand)
        else:
            hand_ranks[RANKS['high card']].append(hand)
    
    # decide between same RANKS
    hands_sorted = []
    for rank, hands in hand_ranks.items():
        if len(hands) > 1:
            rank_hands_sorted = sorted(hands, key=lambda hand: [ORDER[c] for c in hand])
            hands_sorted+=rank_hands_sorted
        elif hands:
            hands_sorted.append(str(hands[0]))

    total_score = 0
    for hand, score in hand_scores.items():
        rank = hands_sorted.index(hand)+1
        total_score += rank*score
        
    return total_score # 248422077

def part2():
    hand_ranks = {}
    hand_scores = {}
    for rank in range(1,len(RANKS)+1):
        hand_ranks[rank] = []
        
    for line in lines:
        hand, score = line.split()
        hand_scores[hand]=int(score)
        hand_dict = Counter(hand)
        J_count = hand_dict.pop(JOKER, None)
        # after popping out Jokers, JJJJJ throws an exception
        if J_count:
            try:
                B_count = max(hand_dict.values()) # Best card count, eg the card most often in this hand (except jokers)
                B_key =  max(hand_dict, key=hand_dict.get) # for Joker to become the most often card
                H_key = sorted(hand_dict, key=lambda hand: [ORDER_2[c] for c in hand])[-1]# for Joker to become the highest card from hand

                if J_count == 4 or J_count == 3: 
                    hand_dict[B_key] += J_count
                elif J_count == 2: 
                    if B_count == 2 or B_count == 3:
                        hand_dict[B_key] += J_count
                    else:# B_count == 1:
                        hand_dict[H_key] += J_count
                elif J_count == 1: 
                    if B_count == 4 or B_count == 3:
                        hand_dict[B_key] += J_count
                    elif B_count == 2:
                        if Counter(hand_dict.values())[B_count] == 2: # going for a full house
                            hand_dict[H_key] += J_count
                        else: # going for a three of a kind:
                            hand_dict[B_key] += J_count
                    else: # B_count == 1
                        hand_dict[H_key] += J_count
            except ValueError:
                hand_dict[ACE] = 5 # hand full of Jokers becomes all aces
                pass 
                    
        card_counts = hand_dict.values()
        if 5 in card_counts:
            hand_ranks[RANKS['five of a kind']].append(hand)
        elif 4 in card_counts:
            hand_ranks[RANKS['four of a kind']].append(hand)
        elif 2 in card_counts and 3 in card_counts:
            hand_ranks[RANKS['full house']].append(hand)
        elif 3 in card_counts:
            hand_ranks[RANKS['three of a kind']].append(hand)
        elif Counter(card_counts)[2] == 2:
            hand_ranks[RANKS['two pair']].append(hand)
        elif 2 in card_counts:
            hand_ranks[RANKS['one pair']].append(hand)
        else:
            hand_ranks[RANKS['high card']].append(hand)
    
  
    # decide between same RANKS
    hands_sorted = []
    for rank, hands in hand_ranks.items():
        if len(hands) > 1:
            rank_hands_sorted = sorted(hands, key=lambda hand: [ORDER_2[c] for c in hand])
            hands_sorted+=rank_hands_sorted
        elif hands:
            hands_sorted.append(str(hands[0]))
    total_score = 0
    for hand, score in hand_scores.items():
        rank = hands_sorted.index(hand)+1
        total_score += rank*score
        
    return total_score # 249817836