from gmpy2 import isqrt


def factorize(N, max_iters=2000):
    """Return (p, q) such that p * q = N"""
    A = isqrt(N)
    iters = 0
    while True:
        x_2 = A * A - N
        if x_2 > 0:
            x = isqrt(x_2)
            p = A + x
            q = A - x
            if p * q == N:
                return (p, q)
        A += 1
        iters += 1
        if iters > max_iters:
            return False


def egcd(b, n):
    """returns (gcd(b, n), a, m) such that a*b + n*m == gcd(b, n)"""
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)


def modinv(e, p):
    """return x such that (x * e) == 1 mod p"""
    g, x, _ = egcd(e, p)
    if g != 1:
        raise Exception('gcd(e, p) != 1')
    return x % p


def base_expansion(n, b):
    """Converts integer to bytes"""
    q = n
    digit_list = []
    while q != 0:
        digit_list.append(q % b)
        q = q // b
    return digit_list


def int_to_str(m):
    """Converts integer to ascii string"""
    L = base_expansion(m, 256)
    return "".join(chr(c) for c in L)
