import random
from collections import defaultdict
from copy import deepcopy

class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

class Deck:

    def __init__(self, cards):
        self.cards = cards

    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                cards.append(card)
        return cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.append(card)

    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.label = label
        self.cards = []

class PokerHand(Hand):
    """Represents a poker hand."""

    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter

    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter

    def has_flush(self):
        """Checks whether this hand has a flush."""
        suit_counts = self.get_suit_counts()
        for count in suit_counts.values():
            if count >= 5:
                return True
        return False
    
    def has_straight(self, n=5):
        """Checks whether this hand has a straight with at least `n` cards."""
        counter = self.get_rank_counts()
        aces = counter.get(1, 0) + counter.get(14, 0)
        if aces > 0:
            counter[1] = aces
            counter[14] = aces

        c_ct = 0
        for r in range(1, 15):
            if r not in counter:
                c_ct = 0
            else:
                c_ct += 1
                if c_ct == n:
                    return True
        
        return False
    
    def has_straight_flush(self):
        # partition our hand into a separate hand for each suit
        # check each subhand for a straight and flush
        suit_hands = defaultdict(PokerHand)
        for c in self.cards:
            suit_hands[c.suit].put_card(c)
        for suit_cards in suit_hands.values():
            if suit_cards.has_flush() and suit_cards.has_straight():
                return True
        return False
    
    def has_pair(self):
        counter = self.get_rank_counts()
        for c in counter.values():
            if c >= 2:
                return True
        return False

    # A hand has a full house if it contains three cards of one rank and two cards of another rank.
    def has_full_house(self):
        has_two, has_three = False, False
        for c in self.get_rank_counts().values():
            if c == 2:
                has_two = True
            elif c == 3:
                has_three = True
            if has_two and has_three:
                return True
        return False


good_hand = PokerHand('good_hand')

suit = 0
for rank in range(10, 15):
    card = Card(suit, rank)
    good_hand.put_card(card)

print(good_hand)

print(good_hand.has_straight())

cards = [Card(0, 2),
         Card(0, 3),
         Card(2, 4),
         Card(3, 5),
         Card(0, 7),
        ]

bad_hand = PokerHand('bad hand')
for card in cards:
    bad_hand.put_card(card)

print(bad_hand)

print(bad_hand.has_straight())

straight_and_flush = deepcopy(bad_hand)
straight_and_flush.put_card(Card(0, 6))
straight_and_flush.put_card(Card(0, 9))
print(straight_and_flush)

print(straight_and_flush.has_straight_flush())