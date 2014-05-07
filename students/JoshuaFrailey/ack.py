def ack(m, n):
    u"""Return the Ackermann-Peter function."""
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))