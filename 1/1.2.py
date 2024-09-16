import time
import sys

def summ(a, b):
    if (-1_000_000_000 <= a and a <= 1_000_000_000) and (-1_000_000_000 <= b and b <= 1_000_000_000):
        return a + b**2
    return "Введите числа еще раз"

t_start = time.perf_counter()
a, b = map(int, input().split())
start = time.perf_counter()
result = summ(a, b)
stop = time.perf_counter()
print(result)
print("time: %s ms" % (time.perf_counter() - t_start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(result)
print(f"memory usage: {memory_usage} bytes")