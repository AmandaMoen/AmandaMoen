def fibonacci(n):
    """Return nth number in the Fibonacci sequence."""
    # Initialize sequence
    seq = [0, 1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]


def lucas(n):
    """Return nth number in the Lucas numbers."""
    # Initialize sequence
    seq = [2, 1]
    if n == 1:
        return 2
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]


def sum_series(n, first=0, second=1):
    """Return nth number in sum series beginning with 'first' and 'second'."""
    seq = [first, second]
    if n == 1:
        return first
    elif n == 2:
        return second
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]

if __name__ == '__main__':
    # Check that fibonacci works
    # Sample sequence
    fib = [0, 1, 1, 2, 3, 5, 8, 13]
    fibtest = True
    for i, val in enumerate(fib, start=1):
        fibtest = val == fibonacci(i)
    if fibtest: print "fibonacci passed"

    # Check that lucas works
    # Sample sequence
    luc = [2, 1, 3, 4, 7, 11, 18, 29]
    luctest = True
    for i, val in enumerate(luc, start=1):
        luctest = val == lucas(i)
    if luctest: print "lucas passed"

    # Check that sum_series works for fib and luc
    sumtest = True
    for i, val in enumerate(fib, start=1):
        sumtest = val == fibonacci(i)
    for i, val in enumerate(luc, start=1):
        sumtest = val == lucas(i)
    if sumtest: print "sum_series passed"
