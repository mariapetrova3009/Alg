
with open('input.txt') as f:
    a, b = map(int, f.readline().split())
    summ = a + b
with open('output.txt', 'w') as f:
    f.write(str(summ))
