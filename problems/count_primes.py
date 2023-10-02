def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0

    is_prime =[]
    for i in range(n):
        is_prime.append(True)

    is_prime[1] = False
    is_prime[0] = False

    for number, prime in enumerate(is_prime):
        if prime:
            for k in range(2, n//number + 1):
                if k * number < n:
                    is_prime[k*number] = False
    
    count = 0
    for pos, prime in enumerate(is_prime):
        if prime:
            print(pos)
        count += prime

    return count
                