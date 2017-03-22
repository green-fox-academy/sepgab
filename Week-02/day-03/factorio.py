# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(nr: int):
    factoral = 1
    for i in range(1, nr + 1):
        factoral *= i
    return(factoral)

print(factorio(5))
print(factorio(10))
