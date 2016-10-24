_ = input()
a = map(int, input().split(" "))
b = map(int, input().split(" "))
print(" ".join([str(ai+bi) for ai,bi in zip(a, b)]))
