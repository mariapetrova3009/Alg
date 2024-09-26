import time
start = time.perf_counter()

with open('input.txt') as f:
    ind_list = []
    n = int(f.readline())
    data = f.readline().split()
    array = []
    for i in range(len(data)):
        array.append([i + 1, float(data[i])])

    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1][1] > x[1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x
        lenn = len(array)



with open('output.txt', 'w') as f:
    f.write(str(array[0][0]) + " " + str(array[lenn//2][0]) + " " +  str(array[-1][0]))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))