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

template = "{0:.7f} {1:s} are worth US${2:d}".format(3 / 4, "9", 6)
template

amount = 10
rate = 88.9
currencie = "Pesos"

result = f"{amount}, {currencie} is worth US${amount/rate}"
result

result = f"{amount}, {currencie} is worth US${amount/rate:.2f}"
result

# Bytes e Unicode
val = "español"
val
val_utf8 = val.encode("utf-8")  # mostra representação em bytes

val_utf8
type(val_utf8)

val_utf8.decode()

# Boleanos
int(True)
int(False)

# Casting de tipos

s = "3.14159"
fval = float(s)
type(fval)
float

int(fval)
3

bool(fval)
True

bool(0)
False

# None
a = None
a is None
True

b = 5
b is not None

True


def add_and_Maybe_Multlply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c

    return result


# Datas e horas
from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day

29
dt.minute
30

dt.time()
dt.strftime("%m/%d/%Y %H:%M")
datetime.strptime("20091031", "%Y%m%d")

dt.replace(minute=0, second=0)
dt

dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
delta

dt2
dt + delta

# if, elif e else
a = 5
b = 7
e = 8
d = 4

if (a < b) ^ (e > d):
    print("Made i.t")

# Laços for
sequence = [1, 2, None, 4, None, 5]
total = 0

for value in sequence:
    if value is None:
        continue
    total += value

print(total)

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0

for value in sequence:
    if value == 5:
        break
    total_until_5 += value
print(total_until_5)

# Expressões ternárias
x = 5

a = "Non-negative" if x >= 0 else "Negative"
print(a)