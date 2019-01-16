from random import shuffle

values = range(1,11) + "Jack Queen King".split()
suits = "diamonds clubs hearts spades".split()
deck = ["%s of %s" % (v,s) for v in values for s in suits] + "Big Small".split()
print deck

shuffle(deck)

print deck
print deck[:13]
zhangsan = []
lisi = []
wangwu = []

while deck:
    a = raw_input(deck.pop())


