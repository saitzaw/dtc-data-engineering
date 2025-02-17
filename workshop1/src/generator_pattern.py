def fibonanci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
if __name__ == '__main__':
    fib = fibonanci(10)
    for i in fib:
        print(i)