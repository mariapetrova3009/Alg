import time
start = time.perf_counter()
def merge(arr, l, m, r):
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i, j, k = 0, 0, l

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)

        merge(arr, p, q, r)


with open('../tests/input.txt') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

merge_sort(arr, 0, n - 1)

with open('../tests/output.txt', 'w') as f:
    f.write(' '.join(map(str, arr)))

