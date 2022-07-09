H, W = map(int, input().split())
S = [input() for _ in range(H)]
indices = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            indices.append((i, j))
a, b = indices[0]
c, d = indices[1]
print(abs(a - c) + abs(b - d))
