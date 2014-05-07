def fibonacci(n):
    """Return the nth value in the fibonacci series.

    Arguments:
    n: A nonnegative, nonzero integer.
    Return value: A positive integer.
    """
    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        return True

    def recursive_fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return recursive_fib(n-1) + recursive_fib(n-2)

    if check_value(n):
        return recursive_fib(n)

if __name__ == "__main__":
    fibonacci_vals = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144)
        ]

    for input_, output in fibonacci_vals:
        assert fibonacci(input_) == output

    for badval in [-1, -2.78, 3.14, 'a', []]:
        try:
            fibonacci_result = fibonacci(badval)
            # lucas_result = lucas(badval)
            # sum_series_result = sum_series(badval)
        except ValueError:
            pass
        else:
            print u"A bad value did not trigger a ValueError!"

    print u"All tests passed!"