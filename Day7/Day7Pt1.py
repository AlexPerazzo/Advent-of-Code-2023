CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def main():
    
    all_cards = [[],[],[],[],[],[],[]]
    sorted_all_cards = []


    with open("Day7/Day7input.txt") as file:
        for line in file:
            
            hand_points = line.split(" ")
            hand = hand_points[0]
            points = hand_points[1]

            value = check_hand(hand)
            all_cards[value].append(hand + ' ' + points.strip())
        
                


            
        # print(all_cards)
        for list_of_cards in all_cards:

            sorted_all_cards.append(sort_hands(CARDS, list_of_cards))

        combined_list = []

        for sublist in sorted_all_cards:
            combined_list += sublist

        all_points = calculate_points(combined_list)  
        print(all_points)
        


def calculate_points(sorted_all_cards):
    all_points = 0
    for i in range(0, len(sorted_all_cards)):
        all_points += int(sorted_all_cards[i][6:]) * (i + 1)
    return all_points

def sort_hands(CARDS, hands_points):
    
    def sort_helper(hand):
        number = ""
        for i in range(len(hand)):
            

            if CARDS.index(hand[i]) < 10:
                number += str(CARDS.index(hand[i]))
            elif CARDS.index(hand[i]) == 10:
                number += "A"
            elif CARDS.index(hand[i]) == 11:
                number += "B"
            elif CARDS.index(hand[i]) == 12:
                number += "C"

        return number
    
    sorted_cards = sorted(hands_points, key=lambda x: sort_helper(x[:5]))
    return sorted_cards


def check_hand(hand):
    #return value of hand with HighCard being 0 and Five of a Kind being 6
    the_set = set()
    for card in hand:
        the_set.add(card)
    
    if len(the_set) == 5:
        #High card
        return 0
    
    if len(the_set) == 4:
        #One pair
        return 1
    
    if len(the_set) == 3:
        #two pair or three of a kind
        the_set2 = set()
        for card2 in hand:
            if card2 in the_set2:
                the_set2.remove(card2)
            else:
                the_set2.add(card2)

        if len(the_set2) == 1:
            #two pair
            return 2
        
        else:
            #three of a kind
            return 3

    
    if len(the_set) == 2:
        #Full house or four of a kind
        sorted_cards = sorted(hand)
        if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]) or (sorted_cards[0] == sorted_cards[1] and sorted_cards[2] == sorted_cards[3] == sorted_cards[4]):
            #Full House
            return 4
        
        else:
            #Four of a kind
            return 5

    if len(the_set) == 1:
        # Five of a Kind
        return 6



main()