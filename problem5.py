#!/usr/bin/env python3

from collections import Counter
from functools import lru_cache, reduce
from itertools import chain, repeat, starmap
from operator import mul

primes = [2, 3, 5, 7, 11, 13, 17, 19]


def ifactors(n):
    result = []
    while n > 1:
        for p in primes:
            if n % p == 0:
                result.append(p)
                n //= p

    return result


@lru_cache()
def factors():
    primes_counter = Counter(primes)

    for n in range(1, 21):
        r = ifactors(n)
        print(f"{n}, factors={r}, {Counter(r) - primes_counter}")
        primes_counter += Counter(r) - primes_counter

    return list(chain.from_iterable(starmap(repeat, primes_counter.items())))


if __name__ == "__main__":
    print(factors())
    print(reduce(mul, factors()))
