for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        print("YES " + ("EVEN" if not len(s) % 2 else "ODD"))
    else:
        print("NO")
