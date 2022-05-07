N, K = map(int, input().split())

for _ in range(K):
    g1 = int("".join(sorted(str(N), reverse=True)))
    g2 = int("".join(sorted(str(N))))
    N = g1 - g2

print(N)
