S, k = input().split(" ")
k = int(k)

suffices = sorted([S[i:] for i in range(len(S))])
print(suffices[k-1])
