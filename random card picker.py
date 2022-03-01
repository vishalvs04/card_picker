import random
cards=['Diamond','Spade','Hearts','Club']
ranks=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
def random_card_pick():
    card=random.choices(cards)
    rank=random.choice(ranks)
    print("The",rank,"of",card)