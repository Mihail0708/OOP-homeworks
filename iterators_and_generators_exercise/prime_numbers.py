def get_primes(data):

    for num in data:
        is_prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

