def count_and_merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = arr[p:q+1]
    R = arr[q + 1: r + 1]

    res = 0
    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            res += n1 - i
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return res

def count_inv(arr, l, r):
    res = 0
    if l < r:
        q = (r + l) // 2
        res += count_inv(arr, l, q)
        res += count_inv(arr, q + 1, r)
        res += count_and_merge(arr, l, q, r)

    return res

with open('../tests/input.txt') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

count = count_inv(arr, 0, n - 1)

with open('../tests/output.txt', 'w') as f:
    f.write(str(count))

