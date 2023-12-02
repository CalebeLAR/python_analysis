seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]
seq3 = [True, False]

zipped = zip(seq1, seq2, seq3)

print(list(zipped))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print("{0}: {1}, {2}".format(i, a, b))

pitchers = [("Nolan", "Ryan"), ("Roger", "Clemens"), ("Schilling", "Curt")]
first_names, last_names = zip(*pitchers)

print(f"first_names: {first_names}")
print(f"last_names: {last_names}")
