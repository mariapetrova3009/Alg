import time
def selection_sort(n, array):
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if array[j] < array[min_ind]:
                min_ind = j

        array[i], array[min_ind] = array[min_ind], array[i]
    return array


start = time.perf_counter()
with open('../tests/input.txt') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().split()))
    result = selection_sort(n, array)

with open('../tests/output.txt', 'w') as f:
    f.write(' '.join(map(str, result)))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))
