# function return function a => (b) => void
def make_incrementor(n):
    return lambda x : x + n;
x = make_incrementor(10)
b = x(2)
print(b)