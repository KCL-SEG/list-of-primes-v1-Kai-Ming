"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    pointer = 1
    counter = 0
    while counter < number_of_primes:
        pointer += 1
        is_prime = True
        for num in list:
            if pointer % num != 0:
                is_prime = True
            else:
                is_prime = False
                break
        if is_prime:
            list.append(pointer)
            counter += 1
    print(list)
    return list

#primes(3)