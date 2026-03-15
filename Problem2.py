from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

s = sorted(s)


for j in combinations_with_replacement(s, k):
        print(''.join(j))
