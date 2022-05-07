N = int(input())
A = []
B = []
for _ in range(N):
    s = input().split()
    A.append(int(s[0]))
    B.append(int(s[1]))

for a, b in zip(A, B):
    new_A = A.copy()
    new_B = B.copy()
    new_A.remove(a)
    new_B.remove(b)
    if all([a + b < c for c in new_A + new_B]):
        print(a + b)
        exit()

if A.index(min(A)) == B.index(min(B)):
    if sorted(A)[1] < sorted(B)[1]:
        print(max(sorted(A)[1], min(B)))
    else:
        print(max(min(A), sorted(B)[1]))
else:
    print(max(min(A), min(B)))
