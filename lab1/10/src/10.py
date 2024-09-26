import time
start = time.perf_counter()
with open('../tests/input.txt') as f:
    n = int(f.readline())
    s = f.readline()
    sl = {}
    for el in s:
        if el not in sl:
            sl[el] = 1
        else:
            sl[el] += 1
    answer = ""
    letter = ""
    for k, v in sorted(sl.items()):
        if v % 2 == 0:
            while v > 0:
                answer = answer[:len(answer) // 2] + k + k + answer[len(answer)//2:]
                v -= 2
        else:
            if letter == "":
                letter = k
    answer = answer[:len(answer) // 2] + letter + answer[len(answer)//2:]

with open('../tests/output.txt', 'w') as f:
    f.write(answer)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))
