import sys
import random
import hashlib

from random import randint as rnd

# Fixed Random Seed
hashValue = hashlib.sha256("|".join(sys.argv[1:]).encode()).hexdigest()
random.seed(hashValue)

Nl = 75; Nr = 100; nl = 1; nr = 10**4

print(rnd(Nl, Nr), rnd(nl, nr))