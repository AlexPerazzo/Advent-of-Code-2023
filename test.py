
hand = "LJJ..LL-7J.F.JJ7-L|JJJ.L-L.L-..JJLLLJ-F-L--L-|-LJL---JLJ-LJLLJL7JJL-7LL-|J.-JJ|JL--F-|LFFLJ-7LL--J-|JJ.7-LF-J7.LJJF-J-|.LFFJFFJJ.FJLJ-LJ.LJ7"

print(len(hand))













# CARDS = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


# def main():
#     hand = "AAAJA 123"
#     poss = one_joker(hand, 3)
#     print(poss)
        

# def joker(CARDS, hand):

#     return

# def one_joker(hand_points, index_of_J):
#     possible_hands = []
#     hand_list = list(hand_points)
#     for possible_card in CARDS[1:]:
#         hand_list[index_of_J] = possible_card
#         possible_hands.append("".join(hand_list))

    
#     return possible_hands

    

    




# def calculate_points(sorted_all_cards):
#     all_points = 0
#     for i in range(0, len(sorted_all_cards)):
#         all_points += int(sorted_all_cards[i][6:]) * (i + 1)
#     return all_points

# def sort_hands(CARDS, hands_points):
    
#     def sort_helper(hand):
#         number = ""
#         for i in range(len(hand)):
            

#             if CARDS.index(hand[i]) < 10:
#                 number += str(CARDS.index(hand[i]))
#             elif CARDS.index(hand[i]) == 10:
#                 number += "A"
#             elif CARDS.index(hand[i]) == 11:
#                 number += "B"
#             elif CARDS.index(hand[i]) == 12:
#                 number += "C"

#         return number
    
#     sorted_cards = sorted(hands_points, key=lambda x: sort_helper(x[:5]))
#     return sorted_cards


# def check_hand(hand):
#     #return value of hand with HighCard being 0 and Five of a Kind being 6
#     the_set = set()
#     for card in hand:
#         the_set.add(card)
    
#     if len(the_set) == 5:
#         #High card
#         return 0
    
#     if len(the_set) == 4:
#         #One pair
#         return 1
    
#     if len(the_set) == 3:
#         #two pair or three of a kind
#         the_set2 = set()
#         for card2 in hand:
#             if card2 in the_set2:
#                 the_set2.remove(card2)
#             else:
#                 the_set2.add(card2)

#         if len(the_set2) == 1:
#             #two pair
#             return 2
        
#         else:
#             #three of a kind
#             return 3

    
#     if len(the_set) == 2:
#         #Full house or four of a kind
#         sorted_cards = sorted(hand)
#         if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]) or (sorted_cards[0] == sorted_cards[1] and sorted_cards[2] == sorted_cards[3] == sorted_cards[4]):
#             #Full House
#             return 4
        
#         else:
#             #Four of a kind
#             return 5

#     if len(the_set) == 1:
#         # Five of a Kind
#         return 6



# main()