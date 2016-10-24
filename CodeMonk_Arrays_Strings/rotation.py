for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    print(" ".join(map(str, a[-k%n:] + a[:-k%n])))
