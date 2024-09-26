import time
def bubble_sort(n, array):
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag == False:
            break
    return array


start = time.perf_counter()
with open('input.txt') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().split()))
    result = bubble_sort(n, array)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, result)))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))
