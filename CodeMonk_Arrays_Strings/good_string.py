s, i = input(), 0
l, good = len(s), 0
while i < l:
    while i < l and (s[i] not in ['a', 'e', 'i', 'o', 'u']):
        i += 1
    if i < l:
        counter = 0
        while i < l and s[i] in ['a', 'e', 'i', 'o', 'u']:
            i += 1
            counter += 1
        if counter > good:
            good = counter

print(good)
