import timeit
import gc
import random

def coin_toss():
    return random.choice([True, False])

t = timeit.Timer('coin_toss()', globals=globals()) # without GC
# t = timeit.Timer('coin_toss()', 'gc.enable()', globals=globals()) # with GC
print(t.timeit(number=10000)) # nuymber of times to run the function
print(t.autorange())
