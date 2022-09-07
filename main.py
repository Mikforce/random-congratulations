#!/usr/bin/env python3
import random
from text import *

# , C, be, let
def ran(dear, wish, be, empty):
    item = random.SystemRandom().choice(dear)
    item1 = random.SystemRandom().choice(wish)
    item2 = random.SystemRandom().choice(be)
    item3 = random.SystemRandom().choice(empty)
    return item, item1, item2, item3
rez = ran(dear = dear, wish = wish, be = be, empty = empty)




print(str(rez))

