def compute_GCD(a: int, b: int) -> int:
    """Compute Greatest Common Divisor.

    Args:
        a (int): nonnegative integer
        b (int): nonnegative integer

    Returns:
        int: Greatest Common Divisor
    """
    if a < b:
        a, b = b, a

    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b

    return b


if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd = compute_GCD()
    print(gcd)
