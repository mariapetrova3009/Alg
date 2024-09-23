import time
import sys


start = time.perf_counter()

with open('input.txt') as f:
    a, b = map(int, f.readline().split())
    if (-1_000_000_000 <= a and a <= 1_000_000_000) and (-1_000_000_000 <= b and b <= 1_000_000_000):
        summ = a + b**2
    else:
        print("Введите числа еще раз")

with open('output.txt', 'w') as f:
    f.write(str(summ))
stop = time.perf_counter()
print("time: %s ms" % (stop - start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(summ)
print(f"memory usage: {memory_usage} bytes")