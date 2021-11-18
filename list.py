from modules.fibo import fib


def s_Square(n) :
    return n**2
squares = list(map(s_Square, range(10)))
print(squares)
