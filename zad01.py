A = {1,2,3,4,5}
B = {2,4,6,8,10}

print(f"Suma: {A | B}")

print(f"Przeciecie: {A&B}")

print(f"Roznica symetryczna {A^B}")

print(f"Czy element 10 jest w A: {10 in A}")

repeated_arr: list[int] = [1,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]

uniq_arr: set[int] = set[int](repeated_arr)

print(f"Lista z powtarzalnymi wartościami: {repeated_arr}")

print(f"Zbiór z unikatowymi wartościami {uniq_arr}")