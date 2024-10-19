import time
start = time.perf_counter()
def max_subarray(arr):
    max_current = maxx = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > maxx:
            maxx = max_current

    return maxx

with open('../tests/input.txt') as f:
    arr = list(map(int, f.readline().split()))
    ans = max_subarray(arr)
with open('../tests/output.txt', 'w') as f:
    f.write(str(ans))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))