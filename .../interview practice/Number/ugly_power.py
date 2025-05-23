# A Hamming Number (also called an ugly number) is any positive integer that has its set of prime factors as a subset of the prime numbers 2, 3, and 5. On the other hand, a prime power is produced using any integer 
# k raised to a prime p and is represented as p^k. As such, we can create a theoretical term, an “ugly power,” which is any ugly number multiplied by any arbitrary positive integer k. We can represent this by having any ugly number h, and an ugly power be h^k
# Write a function ugly_powers(s: set) -> bool which takes a set s and returns a boolean value determining whether or not all the elements of set s are all ugly powers.


def is_ugly(n: int):
    while n != 1:

        if n% 3 == 0:
            n //= 3
            continue

        if n % 5 == 0:
            n //= 5
            continue

        if n % 2 == 0:
            n //= 2
            continue

        return False

    return True

def ugly_powers(s: set) -> bool:
    return all([is_ugly(x) for x in s])

print(ugly_powers({1, 2, 5, 10}))

'''time complexity: is_ugly O(log n)
