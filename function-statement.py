def fibonaci(n):
    """Print fibonaci array from 1 to n"""
    a,b = 1,1
    while(a < n):
        print(a)
        a,b = b, a + b
# fibonaci(10)
# * arguments : params
# ** keywords : params object {key : value}
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
# cheeseshop("Limburger",
#             "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            "It's really very, VERY runny, sir2.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch",
#            keyword2="name")
# normal agument
def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
standard_arg(arg="3")
standard_arg("3")
pos_only_arg("3")
# pos_only_arg(arg="3") #not run
kwd_only_arg(arg=3)
# kwd_only_arg(3) #not run
combined_example(2, standard=4, kwd_only=5)
