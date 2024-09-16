import time
import sys

def summ(a, b):
    return a + b

t_start = time.perf_counter()
a, b = map(int, input().split())
start = time.perf_counter()
result = summ(a, b)
stop = time.perf_counter()
print(result)
duration_microseconds = (stop - start) * 1_000_000
print("time: %s ms" % (time.perf_counter() - t_start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(result)
print(f"memory usage: {memory_usage} bytes")