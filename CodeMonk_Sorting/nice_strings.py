N = int(input())
strings = [input() for _ in range(N)]
for i, s in enumerate(strings):
    print(len([x for x in strings[:i+1] if x < s]))
