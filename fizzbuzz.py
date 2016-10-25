def zz(n):
    s = (int(n % 3 == 0) * 'Fizz') + (int(n % 5 == 0) * 'Buzz')
    return str(n) if s == '' else s

_ = input()
nn = list(map(int,input().split(" ")))
print("\n".join(["\n".join([zz(x) for x in range(1, n+1)]) for n in nn]))
