import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
for comb in itertools.combinations(A, 2):
    ans += (comb[0] - comb[1]) ** 2

print(ans)
