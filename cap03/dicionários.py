from collections import defaultdict

dicionario = {"key": "value"}
print(dicionario)

dicionario.update({"key2": "value2", "key": "another value"})
print(dicionario)

words = ["apple", "bat", "bar", "atom", "book"]
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

print(by_letter)

by_letter = {}
for word in words:
    letter = word[0]
    # by_letter.setdefault(letter, []).append(word)
    by_letter.setdefault(letter, []).append(word)

print(by_letter)


key = "z"
if key in by_letter:
    value = by_letter[key]
    print(f"value: {value}")
else:
    value = "default value"
    print(f"value: {value}")

value = by_letter.get(key, "default value")
print(value)


by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)

print(by_letter)