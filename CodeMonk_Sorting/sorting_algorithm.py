def chunk(ai, i):
    return (ai[::-1][5*(i-1):5*i])[::-1]

def calculate_chunks(A, i):
    Arr = sorted([(chunk(ai, i), j, ai) for j, ai in enumerate(A)])
    weight, A = 0, []
    for c, _, ai in Arr:
        weight += int(c) if c else 0
        A.append(ai)
    return weight, A

if __name__ == "__main__":
    N = int(input())
    A = input().split(" ")
    weight, i = sum(map(int, A)), 1
    while True:
        weight, A = calculate_chunks(A, i)
        if weight == 0:
            break
        print(" ".join(A))
        i += 1

