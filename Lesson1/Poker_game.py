'''
hand = 5 cards.
card = (rank,suit)

creat function take hands and return the best hand ==> poker(hands) -> hand
hand rank function rank each hand based on
n_kind : 2 repeated in each kind (suit doesn't matter)
straignt : increasing sequence of ranks (suit doesn't matter)
flush : All 5 cards have the same suit (the rank doesn't matter)
'''

def poker(hands):
    ''' take list of hands and return list of all winning hands poker([hand ...]) => [hand,..] '''
    return allmax(hands,key=hand_rank)
def allmax(iterable,key=None):
    ''' Return a list of all items equal to the max of the iterable '''
    result,maxval = [],None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result,maxval = [x],xval
        elif xval == maxval:
            result.append(x)
    return result
    '''
    q = []
    m_hand = max(iterable,key=key)
    m_rank = key(m_hand)
    for x in iterable:
        res = key   (x)
        if res == m_rank :
            q.append(x)
    return q
    '''

def card_ranks(hand):
    '''Return a list of the ranks sorted with higher first'''
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def straight(ranks):
    ''' Retrun true if the ordered ranks from a 5-card straignt'''
    return (max(ranks)-min(ranks)==4) and len(set(ranks))==5
    '''
    for i in range(len(ranks)-1):
        if ranks[i] != ranks[i+1]+1:
            return False
    return True
    '''

def flush(hand):
    ''' Return true if all the cards have the same suit '''
    suits = [s for r,s in hand]
    return len(set(suits))==1

    '''
    s = suits[0]
    for i in range(len(suits)):
        if suits[i] != s:
            return False
    return True
    '''

def hand_rank(hand):
    '''Return a value indicating the ranking of a hand'''
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8,max(ranks))
    elif kind(4,ranks):
        return (7,kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks): # full house
        return (6,kind(3,ranks),kind(2,ranks))
    elif flush(hand):
        return (5,ranks)
    elif straignt(ranks):
        return (4,max(ranks))
    elif kind(3,ranks):
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):
        return (2,two_pair(ranks),ranks)
    elif kind(2,ranks):
        return (1,kind(2,ranks),ranks)
    else:
        return (0,ranks)

def kind(n,ranks):
    ''' Return the first rank that this hand has exactly n of
    Return None if there is no n-of-a-kind in the hand.'''
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    ''' If there are two pair, return two ranks as tuple
    (heighest,lowest); otherwise return None.'''
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    if pair and pair != lowpair:
        return (pair,lowpair)
    else:
        return None
    '''
    q = []
    for r in set(ranks):
        if ranks.count(r) == 2:
            q.append(r)
    if len(q) < 2:
        return None
    else:
        return (max(q),min(q))
    '''

def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4,fkranks) == 9
    assert kind(3,fkranks) == None
    assert kind(2,fkranks) == None
    assert kind(1,fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)

    sfranks = card_ranks(sf)
    assert straight(sfranks) == True
    assert straight(fkranks) == False
    assert flush(sf) == True
    assert flush(fk) == False

    assert poker([sf,fk,fh]) == sf
    assert poker([fh,fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf]+99*[fh]) == sf

    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)

    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    print "test Pass"
test()
import random
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands,n=5,deck=mydeck):
    ''' Return number of player with cards for each player'''
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    '''
    players = []
    for p in range(numhands):
        players.append(deck[n*p : (n*p)+n])
    return players
    '''
