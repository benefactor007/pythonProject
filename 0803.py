# coding=utf-8

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

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same ... check ranks

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
        return 0

    # def __cmp__(self, other):
    #     return cmp((self.suit, self.rank), (other.suit, other.rank))


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

    def shuffling(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            """
            random.randrange ([start,] stop [,step])
            start -- 指定范围内的开始值，包含在范围内。 
            stop -- 指定范围内的结束值，不包含在范围内。 
            step -- 指定递增基数。 
            """
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            print "Remove", card, "successfully"
            return True
        else:
            print "This card,", card, "has been removed"
            return False

    def popCard(self):
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        return self.cards.pop()

    def insertCard(self, card):  # insert the card to the first position
        self.cards.insert(0, card)

    """
    list.insert(index, obj)
    index -- 对象 obj 需要插入的索引位置。
    obj -- 要插入列表中的对象。
    """

    def deal(self, hands, nCards=999):
        nHands = len(hands)
        for i in range(nCards):
            # print "The current length of self.cards is", len(self.cards)
            if self.isEmpty(): break  # break if out of cards
            card = self.popCard()  # take the top card
            hand = hands[i % nHands]  # whose turn is next?
            # print "The current hand is", hand
            hand.addCard(card)  # add the card to the hand

    def isEmpty(self):
        return len(self.cards) == 0


class Hand(Deck):
    def __init__(self, name=""):  # initialize the attributes for the hand
        # Deck.__init__(self)
        self.cards = []
        self.name = name

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains\n " + Deck.__str__(self)

"""
deck = Deck()
deck.shuffling()
print deck
print "len(deck.cards) is", len(deck.cards)
hand1 = Hand("Dynasty")
hand2 = Hand("Lu")
hand3 = Hand("Wu")
deck.deal([hand1, hand2, hand3], 52)
    # print hand1
    # print hand2
    # print hand3
print "%s \n %s \n %s \n " %(hand1,hand2,hand3)
    # print "%s %s %s " %(hand1,hand2,hand3)
"""

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffling()


newGame = CardGame()
print newGame.deck