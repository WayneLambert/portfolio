# List prime numbers between 2 and 100

prime_numbers = []

def is_prime(number):
    """ Determines whether given number is prime or not """
    for factor in range(2, number):
        if number % factor == 0:
            return False
        return True

def get_prime_numbers(max_num):
    """ Builds list of prime numbers up to a maximum of max_num """
    for tested_num in range(2, max_num):
        if is_prime(tested_num):
            prime_numbers.append(tested_num)
    return prime_numbers


if __name__ == '__main__':
    prime_numbers = get_prime_numbers(100)
    print(prime_numbers)
