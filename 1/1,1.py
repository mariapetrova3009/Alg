import time
import sys

def summ(a, b):
    return a + b

a, b = map(int, input().split())
start = time.perf_counter()
result = summ(a, b)
stop = time.perf_counter()
print(result)
print("time: %s ms" % (time.perf_counter() - start))
memory_usage = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(result)
print(f"memory usage: {memory_usage} bytes")