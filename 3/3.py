import time
t_start = time.perf_counter()
with open('input.txt') as f:
    n = int(f.readline())
    el1 = 0
    el2 = 1
    for i in range(2, n + 1):
        c = el2
        el2 = (el1 + el2) % 10
        el1 = c
with open('output.txt', 'w') as f:
    f.write(str(el2))

print("Время работы %s секунд " % (time.perf_counter() - t_start))
