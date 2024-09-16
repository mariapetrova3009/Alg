import time
import sys


t_start = time.perf_counter()
start = time.perf_counter()

with open('input.txt') as f:
    a, b = map(int, f.readline().split())
    summ = a + b**2
with open('output.txt', 'w') as f:
    f.write(str(summ))
stop = time.perf_counter()
duration_microseconds = (stop - start) * 1_000_000
print("time: %s ms" % (time.perf_counter() - t_start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(summ)
print(f"memory usage: {memory_usage} bytes")