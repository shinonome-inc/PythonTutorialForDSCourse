from math import sqrt


def is_prime(n: int) -> bool:
    """Determines if the given number is prime.

    Args:
        n (int): Nonnegative integer.
    Returns:
        bool: If n is prime, then True else False
    """
    max_num = int(sqrt(n))
    _is_prime = True
    for m in range(2, max_num + 1):
        r = n % m
        if r == 0:
            _is_prime = False
            break
    return _is_prime  # できればreturnをつかってほしい


if __name__ == "__main__":
    n = int(input())
    _is_prime = is_prime(n)
    if _is_prime:
        print("素数")
    else:
        print("素数じゃない")
