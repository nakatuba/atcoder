X = input()
M = int(input())
n = int(max(X)) + 1
ans = 0
while int(X, base=n) <= M:
    n += 1
    ans += 1

print(ans)
