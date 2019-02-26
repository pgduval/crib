import itertools as it
import random

# Generate deck
def make_deck():
    suits = ['h', "d", "c", "s"]
    ranks = range(2, 15)

    deck = []
    for r in ranks:
        for s in suits:
            deck.append((r, s))
    return deck

def get_ranks(hand):
    ranks = []
    for r, _ in hand:
        if r > 10:
            r = 10
        ranks.append(r)
    return ranks

def get_suits(hand):
    suits = []
    for _, s in hand:
        suits.append(s)
    return suits

def remove(hand, cardsToRemove):
    if not isinstance(cardsToRemove, list):
        cardsToRemove = list(cardsToRemove)
    remaining_cards = []
    for h in hand:
        if h not in cardsToRemove:
            remaining_cards.append(h)
    return remaining_cards

def print_combi(l, k):
    for i in it.combinations(l, k):
        print(i)

# print_combi(['r1', 'r2', 'r3', 'r4'], 3)

# Scoring fonctions

def check_pairs(hand, cut):
    pts_pair = 0
    for h in it.combinations(list(hand) + [cut], 4):
        hand_ranks = get_ranks(h)
        if (hand_ranks.count(hand_ranks[0]) == len(hand_ranks)):
            # pass
            return 12
    for h in it.combinations(list(hand) + [cut], 3):
        hand_ranks = get_ranks(h)
        if (hand_ranks.count(hand_ranks[0]) == len(hand_ranks)):
            pts_pair += 6
            hand = remove(hand, h)

    for h in it.combinations(list(hand) + [cut], 2):
        hand_ranks = get_ranks(h)
        if (hand_ranks.count(hand_ranks[0]) == len(hand_ranks)):
            pts_pair += 2
    return pts_pair


all_5_connectors = [[v, v + 1, v + 2, v + 3, v + 4] for v in range(1, 7)]
all_4_connectors = [[v, v + 1, v + 2, v + 3] for v in range(1, 8)]
all_3_connectors = [[v, v + 1, v + 2] for v in range(1, 9)]
def check_connectors(hand, cut):
    pts_connector = 0
    hand_ranks = get_ranks(list(hand) + [cut])
    if hand_ranks in all_5_connectors:
        return 5
    for h in it.combinations(list(hand) + [cut], 4):
        hand_ranks = get_ranks(h)
        if hand_ranks in all_4_connectors:
            pts_connector += 4
            hand = remove(hand, h)
    for h in it.combinations(list(hand) + [cut], 3):
        hand_ranks = get_ranks(h)
        if hand_ranks in all_3_connectors:
            pts_connector += 3
            hand = remove(hand, h)
    return pts_connector


def check_suits(hand, cut):
    pts_suits = 0
    for h in it.combinations(list(hand) + [cut], 5):
        hand_suits = get_suits(h)
        if (hand_suits.count(hand_suits[0]) == len(hand_suits)):
            return 5
    for h in it.combinations(list(hand) + [cut], 4):
        hand_suits = get_suits(h)
        if (hand_suits.count(hand_suits[0]) == len(hand_suits)):
            pts_suits += 4
    return pts_suits


def check_15(hand, cut):
    pts_15 = 0
    for h in it.combinations(list(hand) + [cut], 5):
        hand_ranks = get_ranks(h)
        if sum(hand_ranks) == 15:
            pts_15 += 2
    for h in it.combinations(list(hand) + [cut], 4):
        hand_ranks = get_ranks(h)
        if sum(hand_ranks) == 15:
            pts_15 += 2
    for h in it.combinations(list(hand) + [cut], 3):
        hand_ranks = get_ranks(h)
        if sum(hand_ranks) == 15:   
            pts_15 += 2            
    for h in it.combinations(list(hand) + [cut], 2):
        hand_ranks = get_ranks(h)
        if sum(hand_ranks) == 15: 
            pts_15 += 2                           
    return pts_15


def check_noob(hand, cut):
    _, cs = cut
    if (11, cs) in hand:
        return 1
    else:
        return 0

def score_hand(hand, cut, verbose=False):

    pts_15 = check_15(hand, cut)
    pts_pair = check_pairs(hand, cut)
    pts_connector = check_connectors(hand, cut)
    pts_suits = check_suits(hand, cut)
    pts_noob = check_noob(hand, cut)

    pts_total = sum([pts_15, pts_pair, pts_connector, pts_suits, pts_noob])
    if verbose is True:
        print("-" * 15)
        print("Hand: ", hand)
        print("Cut: ", cut)
        print("Pts 15: ", pts_15)
        print("Pts Pair: ", pts_pair)
        print("Pts Connectors: ", pts_connector)
        print("Pts Suits: ", pts_suits)
        print("Pts Noob: ", pts_noob)
        print("Pts Total: ", pts_total)
        print("-" * 15)


score_hand(hand=((2, 'h'), (2, 'd'), (2, 's'), (2, 'h')), 
           cut=(3, 'h'),
           verbose=True)

score_hand(hand=((11, 'h'), (5, 'd'), (5, 's'), (5, 'c')), 
           cut=(5, 'h'),
           verbose=True)


score_hand(hand=((10, 's'), (7, 'd'), (2, 'd'), (2, 'c')), 
           cut=(5, 'h'),
           verbose=True)



print(get_ranks(hand=((11, 'h'), (5, 'd'), (5, 's'), (5, 'c'), (5, 'h'))))

print(check_pairs(hand=((2, 'h'), (2, 'd'), (2, 's'), (2, 'h')), cut=(3, 'h')))
print(check_pairs(hand=((2, 'h'), (2, 'd'), (2, 's'), (3, 'h')), cut=(3, 'h')))
print(check_pairs(hand=((2, 'h'), (2, 'd'), (3, 's'), (3, 'h')), cut=(3, 'h')))
print(check_pairs(hand=((2, 'h'), (2, 'd'), (3, 's'), (3, 'h')), cut=(6, 'h')))

print(check_connectors(hand=((1, 'h'), (2, 'd'), (3, 's'), (4, 'h')), cut=(5, 'h')))
print(check_connectors(hand=((1, 'h'), (2, 'd'), (3, 's'), (4, 'h')), cut=(10, 'h')))
print(check_connectors(hand=((1, 'h'), (1, 'd'), (2, 's'), (3, 'h')), cut=(4, 'h')))
print(check_connectors(hand=((1, 'h'), (1, 'd'), (2, 's'), (3, 'h')), cut=(10, 'h')))
print(check_connectors(hand=((1, 'h'), (3, 'd'), (5, 's'), (7, 'h')), cut=(10, 'h')))




print(check_suits(hand=((1, 'h'), (2, 'h'), (3, 'h'), (4, 'h')), cut=(5, 'h')))
print(check_suits(hand=((1, 'h'), (2, 'h'), (3, 'h'), (4, 'h')), cut=(5, 's')))
print(check_suits(hand=((1, 'h'), (2, 'h'), (3, 'h'), (4, 's')), cut=(5, 's')))




print(check_noob(hand=((11, 'h'), (11, 's'), (11, 'd'), (11, 'c')), cut=(5, 'h')))
print(check_noob(hand=((11, 'h'), (5, 's'), (5, 'd'), (5, 'c')), cut=(5, 'h')))
print(check_noob(hand=((11, 'h'), (5, 's'), (5, 'd'), (5, 'c')), cut=(5, 'c')))







for i in it.combinations(list(p_hand) + [cut], 3):
    print(i)


ranks, _ = unpack(p_hand)
cr, cs = cut
for i in it.combinations(ranks + [cr], 3):
    print(i)
    print(i.count(i[0]) == len(i))

print(check_pairs(p_hand, cut))







print_combi(['r1', 'r2', 'r3', 'r4'], 2)

def score_hand(hand):


deck = make_deck()

# Random draw to get the cut
cut = random.choice(deck)

deck2 = list(filter(lambda x: x != cut, deck))

combi = list(it.combinations(deck2, 4))

p_hand = combi[0]

r1, _, r2, _, r3, _, r4, _ = unpack(p_hand)





print(check_pairs(p_hand))


for i in it.combinations(p_hand, 2):
    print(i)
    print(pair(i))

# Remove p_hand from possibilities
op_hand = list(filter(lambda x: remove(x, p_hand), combi))




print(len(cond_combi))



print(len(remaining_hand))


print(combi[1])
print(len(combi))

cond_combi = list(filter(lambda x: remove(x, [(14, 'C'), (12, 'S')]), combi))

print(deck[3])





# Generate counter
def count(label, combi, filt):
    """
    f is a lambda which should return true or false
    itrator stucture is a tuple of 2 hands represented
    as a tupple
    """
    match = list(filter(filt, combi))
    print(match)
    prob = len(match) / len(list(combi))
    print("{}: Prob: {:.5f}".format(label, prob))
    return prob


def unpack(hand):
    """
    Hand structure: ((rank, suit), (ranks, suit))
    """
    h1, h2 = hand
    r1, s1 = h1
    r2, s2 = h2
    return r1, s1, r2, s2


def suited(hand):
    r1, s1, r2, s2 = unpack(hand)
    return s1 == s2


def pair(hand):
    r1, s1, r2, s2 = unpack(hand)
    return r1 == r2


def ge(hand, x):
    r1, s1, r2, s2 = unpack(hand)
    return r1 >= x and r2 >= x


def connected(hand, s=1):
    r1, s1, r2, s2 = unpack(hand)
    connectors = [(v, v - s) for v in range(14, 2, -1)] + [(14, s + 1)]
    return (r1, r2) in connectors or (r2, r1) in connectors




s=1
connectors = [(v, v - s) for v in range(14, 2, -1)] + [(14, s + 1)]
print(connectors)

print(list(range(1, 11)))
print(list(it.combinations(range(1, 11), 4)))

connectors = [(v, v - 1, v - 2) for v in range(11, 2, -1)]



print(connectors)

print(sorted([2, 1, 3, 4]) == [1, 2, 3, 4])


def remove(hand, remove):
    h1, h2 = hand
    return h1 not in remove and h2 not in remove


def has_rank(hand, rank):
    r1, s1, r2, s2 = unpack(hand)
    return r1 in rank or r2 in rank


# Standard opening

def utg(x):
    return (pair(x) and ge(x, 7)) or (suited(x) and connected(x) and ge(x, 10))


print(count('UTG', combi, utg))
print(count('UTG', cond_combi, utg))

print((count('UTG', combi, utg) - count('UTG', cond_combi, utg))/count('UTG', cond_combi, utg))
print(1-count('UTG', cond_combi, utg)/count('UTG', combi, utg))

# main
deck = make_deck()
dict_map = {j: i for i, j in enumerate('23456789TJQKA', start=2)}


combi = list(it.combinations(deck, 2))
cond_combi = list(filter(lambda x: remove(x, [(14, 'C'), (12, 'S')]), combi))


def test():
    EPSILON = 0.001
    deck = make_deck()
    combi = list(it.combinations(deck, 2))
    assert count('AKs (or any specific suited cards)', combi, lambda x: suited(x) and ge(x, 13)) - 0.00302 < EPSILON
    assert count('AA (or any specific pair)', combi, lambda x: ge(x, 14) and pair(x)) - 0.00452 < EPSILON
    assert count('AKs, KQs, QJs, or JTs (suited cards)', combi, lambda x: connected(x) and ge(x, 10) and suited(x)) - 0.0121 < EPSILON
    assert count('AK (or any specific non-pair incl. suited)', combi, lambda x: connected(x) and ge(x, 13)) - 0.0121 < EPSILON
    assert count('AA, KK, or QQ', combi, lambda x: pair(x) and ge(x, 12)) - 0.0136 < EPSILON
    assert count('AA, KK, QQ or JJ', combi, lambda x: pair(x) and ge(x, 11)) - 0.0181 < EPSILON
    assert count('Suited cards, jack or better', combi, lambda x: suited(x) and ge(x, 11)) - 0.0181 < EPSILON
    assert count('AA, KK, QQ, JJ or TT', combi, lambda x: pair(x) and ge(x, 10)) - 0.0226 < EPSILON
    assert count('Suited cards, 10 or better', combi, lambda x: suited(x) and ge(x, 10)) - 0.0302 < EPSILON
    assert count('Suited connectors', combi, lambda x: connected(x) and suited(x)) - 0.0392 < EPSILON
    assert count('Connected cards, 10 or better', combi, lambda x: connected(x) and ge(x, 10)) - 0.0483 < EPSILON
    assert count('Any 2 cards with rank at least queen', combi, lambda x: ge(x, 12)) - 0.0498 < EPSILON
    assert count('Any 2 cards with rank at least jack', combi, lambda x: ge(x, 11)) - 0.0905 < EPSILON
    assert count('Any 2 cards with rank at least 10', combi, lambda x: ge(x, 10)) - 0.143 < EPSILON
    assert count('Connected cards (cards of consecutive rank)', combi, lambda x: connected(x)) - 0.157 < EPSILON
    assert count('Any 2 cards with rank at least 9', combi, lambda x: ge(x, 9)) - 0.208 < EPSILON
    # assert count('Not connected nor suited, at least one 2-9', combi, lambda x: not connected(x) and not suited(x)) - 0.534 < EPSILON


test()




def remove(hand, remove):
    h1, h2, h3, h4 = hand
    return h1 not in remove and h2 not in remove and h3 not in remove and h4 not in remove


def unpack(hand):
    """
    Hand structure: ((rank, suit), (ranks, suit))
    """
    h1, h2, h3, h4 = hand
    r1, s1 = h1
    r2, s2 = h2
    r3, s3 = h3
    r4, s4 = h4
    ranks = [r1, r2, r3, r4]
    suits = [s1, s2, s3, s4]
    # return r1, s1, r2, s2, r3, s3, r4, s4
    return ranks, suits


# def check_pairs(hand):
#     r1, _, r2, _, r3, _, r4, _ = unpack(hand)
#     if (r1 == r2 == r3 == r4):
#         return 12
#     elif (r1 == r2 == r3) or (r1 == r2 == r4) or (r1 == r2 == r4) or (r2 == r3 == r4):
#         return 6
#     elif (r1 == r2) or (r1 == r3) or (r1 == r4) or (r2 == r3) or (r2 == r4) or (r3 == r4):
#         return 2
#     else:
#         return 0

class Hand(object):

    def __init__(self, ĥand):
        self.hand = ĥand
        self.ranks = self.getranks()
        self.suits = self.getsuits()

    def getranks(self):
        ranks = []
        for r, _ in self.hand:
            ranks.append(r)
        return ranks

    def getsuits(self):
        suits = []
        for _, s in self.hand:
            suits.append(s)
        return suits

    def remove(self, cards):
        """ Return hand with cards removed"""
        if not isinstance(cards, list):
            cards = [cards]
        hand = []
        for h in self.hand:
            if h not in cards:
                hand.append(h)
        self.hand = hand
        self.ranks = self.getranks()
        self.suits = self.getsuits()
