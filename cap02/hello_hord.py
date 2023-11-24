# Duck typing
import collections


def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:  # not iterable
        return False


isiterable([])

# Operadores binários e comparações
True ^ True
True | False

a = [1, 2, 3]
b = a
c = list(a)

a is b
a is c
a == c

d = 1
e = 1
e == d
e is d

# Objetos imutáveis e mutáveis
strr = "string"
try:
    strr[0] = "S"
except TypeError:
    None

# Strings
s = "12\\34"
s

s = r"this\has\no\special\characters"
s

Person = collections.namedtuple("Person", ["name", "age"])
maria = Person("Maria", 23)

template = "{0:.7f} {1:s} are worth US${2:d}".format(3/4, "9", 6)
template

amount = 10
rate = 88.9
currencie = "Pesos"

result = f"{amount}, {currencie} is worth US${amount/rate}"
result

result = f"{amount}, {currencie} is worth US${amount/rate:.2f}"
result