def is_prime(func):
    def wrapped(*args):
        result = func(*args)
        d = 2
        while result % d != 0:
            d += 1
        if d == result:
            print("Простое")
            return result
        else:
            print("Составное")
            return result

    return wrapped


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
