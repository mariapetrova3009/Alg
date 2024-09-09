import time
t_start = time.perf_counter()
with open('input.txt') as f:
    n = int(f.readline())
    if n < 0 or n > 45:
        print("Неправильный формат данных")
    el1 = 0
    el2 = 1

    for i in range(2, n + 1):
        c = el2
        el2 = el1 + el2
        el1 = c
with open('output.txt', 'w') as f:
    f.write(str(el2))
print("ремя работы %s секунд " % (time.perf_counter() - t_start))