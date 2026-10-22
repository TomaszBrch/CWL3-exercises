from collections import deque

zgloszenia: list[tuple[int, str]] = [

    (101, "A"),
    (102, "B"),
    (103, "C"),
    (104, "A"),
    (105, "A"),
    (106, "B"),
    (107, "C"),
    (108, "C")
]

kolejka: deque[tuple[int, str]] = deque[tuple[int, str]](zgloszenia)

obsluzone_zgloszenia: dict[str, list[int]] = {}

statystyki: dict[str, int] = {

    "Accepted":len(kolejka),
    "Served": 0,
    "Pending": len(kolejka)


}

licznik = 0

print(f"{'step':<5} | {'id':<4} | {'category':<8} | {'pending':<7}")
print("-" * 33)

while kolejka:
    obsluzone: tuple[int, str] =kolejka.popleft()

    (numer, kategoria) = obsluzone

    licznik += 1

    statystyki["Accepted"] -= 1
    statystyki["Served"] += 1
    statystyki["Pending"] -= 1

    print(f"{licznik:<5} | {numer:<4} | {kategoria:<8} | {statystyki["Pending"]:<7}")

    if kategoria not in obsluzone_zgloszenia:
        _ = obsluzone_zgloszenia.setdefault(kategoria, [])
    
    obsluzone_zgloszenia[kategoria].append(numer)

print("\nPodsumowanie")
print(f"Accepted:{statystyki['Accepted']}, Served:{statystyki['Served']}, Pending:{statystyki['Served']}")

print("\nKategorie")

for kategoria, lista in obsluzone_zgloszenia.items():
    print(f"{kategoria}: {len(lista)}")
