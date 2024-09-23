import time
import sys

t_start = time.perf_counter()

def summ(a, b):
    if (-1_000_000_000 <= a and a <= 1_000_000_000) and (-1_000_000_000 <= b and b <= 1_000_000_000):
        return a + b**2
    return "Введите числа еще раз"


a, b = map(int, input().split())
result = summ(a, b)
stop = time.perf_counter()
print(result)
print("time: %s ms" % (stop - t_start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(result)
print(f"memory usage: {memory_usage} bytes")