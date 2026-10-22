import sys

try:
    with open("tekst.txt", "r") as f:
        tekst = f.read()
except FileNotFoundError:
    print("Error: file does not exist")
    sys.exit()

for c in '.,!?"-':
    tekst = tekst.replace(c, "")


tekst = tekst.lower().split()

uniques: list[str] = []

for word in tekst:
    if word not in uniques:
        uniques.append(word)

counts: list[tuple[int,str]] = []

for unique in uniques:
    count = 0
    for word in tekst:
        if word == unique:
            count += 1
    counts.append((count, unique))

counts.sort(reverse=True)

for i in range(min(5, len(uniques))):
    print(f"{counts[i][1]} - {counts[i][0]} ")

print(f"Unique words: {len(uniques)}")

single_counts = [count for count in counts if count[0] == 1]

print(f"Once: {len(single_counts)} ")