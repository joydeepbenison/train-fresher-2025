def prime_generator(limit):
    primes = []
    for n in range(2, limit+1):
        if all(n % p != 0 for p in primes):
            primes.append(n)
            yield n

for prime in prime_generator(20):
    print(prime)

