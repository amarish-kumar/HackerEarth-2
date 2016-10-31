def partition(A, start, end, K):
    i, piv = start + 1, A[start]
    j = start + 1
    while j <= end:
        if not (A[j] % K > piv % K):
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1

    A[start], A[i-1] = A[i-1], A[start]
    return i-1

def quicksort(A, start, end, K):
    if start < end:
        piv_pos = partition(A, start, end, K)
        quicksort(A, start, piv_pos - 1, K)
        quicksort(A, piv_pos + 1, end, K)

N,K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
quicksort(A, 0, N-1, K)
print(" ".join(map(str, A)))
