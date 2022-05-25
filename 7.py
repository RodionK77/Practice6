# промежуточные значения сохраняются в перменную-память
def memoize_factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:
            print("test")
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))
