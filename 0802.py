#####Sets of object
# coding = utf-8

"""???"""

### Program design
"""
Spades  --> 3
Hearts  --> 2
Diamonds --> 1
Clubs    -->0

Jack --> 11
Queen --> 12
King -->13

"""

import copy


class Card:
    """
    We assign these lists to class attributes at the top of the class definition
    """

    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    # list = copy.deepcopy(rankList)
    # list[1], list[13] = list[13], list[1]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rankList[self.rank] + ' Of ' + self.suitList[self.suit]

    # def __cmp__(self, other):
    #     # check the suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1
    #     # suits are the same ... check ranks
    #
    #     if 2 < self.rank <= 13 and other.rank == 1: return -1
    #     if self.rank == 1 and 2 < other.rank <= 13 : return 1
    #
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1
    #     # ranks are the same... it's a tie
    #     return 0

    def __cmp__(self, other):
        return cmp((self.suit,self.rank),( other.suit,other.rank))


print Card(3, 1)
print Card(3, 8)

"""
Take an attention:
A class attribute is defined outside of any method, and it can be accessed from 
any of the method in the class.


"""
print Card(1, 11)

card2 = Card(0, 13)
print "card2 is", card2
print "The suit of Card2 is", card2.suitList[0]


# card2.suitList[0] = "Swirly Whales"
# print "card2 is", card2
# card3 = Card(0,6)
# print "card3 is", card3

c1 = Card(0, 1)
c2 = Card(0, 13)
c3 = Card(0,2)
c4 = Card(0,1)
print "Card(0,1) > Card(0,13)", c1.__cmp__(c2)
print "Card(0,1) < Card(0,2)", c1.__cmp__(c3)
print "Card(0,1) = Card(0,1)", c1.__cmp__(c4)
print "Card(0,13) < Card(0,1)", c2.__cmp__(c1)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # def __str__(self):
    #     for card in self.cards:
    #         print card

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + '\n'
        return s

    # def shuffle(self):
    #     import random
    #     nCards = len(self.cards)
    #     for i in range(nCards):
    #         j = random.randrange(i, nCards)
    #         self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def shuffle(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            # self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            temp = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = temp

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            print card, "has been removed"
            return True
        else:
            print "There is no", card
            return False


d1 = Deck()
print d1
d2 = Deck()
d2.shuffle()
print d2
d3 = Deck()
d3.removeCard(Card(3, 1))
d3.removeCard(Card(3, 1))
print d3
