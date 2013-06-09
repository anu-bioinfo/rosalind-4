#!/usr/bin/env python

from __future__ import print_function, division
import os
from itertools import permutations, product
import operator


def signed_permutation(n):
    for p in permutations(range(1, n + 1), n):
        for mask in product((-1, 1), repeat=n):
            yield tuple(map(operator.mul, p, mask))


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_sign.txt')) as dataset:
        n = int(dataset.readline().rstrip())
        sign = list(signed_permutation(n))
        print(len(sign))
        for p in sign:
            print(*p, sep=" ")
