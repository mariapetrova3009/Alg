import time
import sys

t_start = time.perf_counter()

with open('input.txt') as f:
    n = int(f.readline())
    el1 = 0
    el2 = 1
    if n < 0 or n > 10**7:
        print("Неправильный формат данных. Введите число еще раз")
    else:

        for i in range(2, n + 1):
            el1, el2 = el2, (el1 + el2) % 10
with open('output.txt', 'w') as f:
    f.write(str(el2))
stop = time.perf_counter()
print("time: %s ms" % (stop - t_start))
memory_usage = sys.getsizeof(n) + sys.getsizeof(el1) + sys.getsizeof(el2)
print(f"memory usage: {memory_usage} bytes")
