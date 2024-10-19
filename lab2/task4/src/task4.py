def bin(arr, l, r, v):
    if l > r:
        return -1
    m = (l + r) // 2
    if v == arr[m]:
        return m
    elif v < arr[m]:
        return bin(arr, l, m - 1, v)
    return bin(arr, m + 1, r, v)

with open('../tests/input.txt') as f:
    n = int(f.readline())
    sort_arr = list(map(int, f.readline().split()))
    k = int(f.readline())
    choice_arr = list(map(int, f.readline().split()))
    ans = []
    for el in choice_arr:
        index = bin(sort_arr, 0, len(sort_arr) - 1, el)
        ans.append(index)
with open('../tests/output.txt', 'w') as f:
    f.write(' '.join(map(str, ans)))

