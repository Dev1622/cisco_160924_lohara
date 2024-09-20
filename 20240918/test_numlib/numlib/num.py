def is_odd(N):
    if N % 2 == 0:
        return False
    return True
def is_even(N):
    if N % 2 != 0:
        return False
    return True
def is_prime(N):
    import math
    N_sqrt = int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N % i == 0:
            return False
    return True