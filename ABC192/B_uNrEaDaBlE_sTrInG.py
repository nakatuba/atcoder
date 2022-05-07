S = input()
print("Yes" if S[::2] == S[::2].lower() and S[1::2] == S[1::2].upper() else "No")
