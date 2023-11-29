# import bisect

# # Tuplas
# # Usando essa funcionalidade, você poderá facilmente trocar nomes de variáveis (fazer swap)
# a, b = "a", "b"
# a, b = b, a
# print("a=>{}, b=>{}".format(a, b))
# print("a=>%s, b=>%s" % (a, b))
# print(f"a=>{a}, b=>{b}")

# # Listas
# print([1, 2, 3, 4, 5, 5, 5].count(5))
# print((1, 2, 3, 4, 5, 5, 5).count(5))

# a = ["boo", "foo", "bar", "buz"]
# a.append("boo")
# print(a)
# a.insert(2, "boo")
# print(a)

# # Ordenação

# b = ["saw", "SfTla l l", "He", "foxes", "si.x"]
# b.sort(key=len)

# # Busca binária e manutenção de uma lista ordenada
# c = [0, 1, 2, 3, 4, 5, 6, 7]
# print(bisect.bisect(c, 2))
# print(c)

# fatiamento
seq = [0, 1, 2, 3, 4, 5, 6, 7]
sev = [7, 6, 5, 4, 3, 2, 1, 0]
print("+ : +", seq[1:5])
print("+ : -", seq[1:-1])
print("- : +", seq[-6:6])
print("- : -", seq[-7:])
print("-------------")
# [inicio - 0: fim - 1]
# [-inicio - 1: fim - 0]

