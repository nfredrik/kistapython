import random

class Card(object):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10


class Suit(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol



def old_card(rank, suit):
    if rank == 1: return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11:'J', 12:'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range")


def card(rank, suit):
    class_ = {1:AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)


Club, Diamond, Heart, Spade = Suit('Club','C'), Suit('Diamond','D'),Suit('Heart','H'), Suit('Spade','S')

deck = [card(rank, suit)
     for rank in range(1, 14)
         for suit in (Club, Diamond, Heart, Spade)]


random.shuffle(deck)

for c in deck:
    print c.rank
    print c.suit.name
