import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    a, b, c = line()
    print(1 - (b+c)%2, 1 - (a+c)%2, 1 - (a+b)%2)