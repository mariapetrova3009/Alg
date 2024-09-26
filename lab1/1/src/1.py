import time
start = time.perf_counter()

with open('../tests/input.txt') as f:
    ind_list = []
    n = int(f.readline())
    array = list(map(int, f.readline().split()))
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x


with open('../tests/output.txt', 'w') as f:
    f.write(' '.join(map(str, array)))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))
