def tribonacci():
    a, b, c = 1, 1, 1
    while True:
        result = a
        a, b, c = b, c, a + b + c
        yield result
        print(result)


t = tribonacci()
i = 0

for i in range(34):
    next(t)
    i += 1
