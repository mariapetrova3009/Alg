def find_majority(arr, l, r):
    if l == r:
        return arr[l]

    m = (l+ r) // 2
    l_majority = find_majority(arr, l, m)
    r_majority = find_majority(arr, m + 1, r)

    if l_majority == r_majority:
        return l_majority

    l_count = sum(1 for i in range(l, r + 1) if arr[i] == l_majority)
    r_count = sum(1 for i in range(l, r + 1) if arr[i] == r_majority)

    return l_majority if l_count > r_count else r_majority

def majority_element(arr):
    cand = find_majority(arr, 0, len(arr) - 1)

    count = sum(1 for num in arr if num == cand)
    if count > len(arr) // 2:
        return 1
    else:
        return 0

with open('../tests/input.txt') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

res = majority_element(arr)

with open('../tests/output.txt', 'w') as f:
    f.write(str(res))

