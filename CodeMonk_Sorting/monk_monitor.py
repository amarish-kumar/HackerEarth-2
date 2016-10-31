T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split(" ")))
    heights = list(set(S))
    m = 0
    for i in range(len(heights)):
        for j in range(len(heights)):
            if i != j:
                d = abs(S.count(heights[i]) - S.count(heights[j]))
                if d > m:
                    m = d

    print(m if m != 0 else -1)
