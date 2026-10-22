S: dict[str, str | int] = {"name":"Tomasz", "age":19, "surname":"Kowalski", "country":"Poland", "birth_year":2007 }

print(S)

S["hobby"] = "music"

print(S)

S["age"] = 20

print(S)

_ = S.pop("hobby")

print(S)

print(S.get("hobby", "key not found"))

print(S.items())

S2: dict[str, str] = {"Warsaw":"Poland", "Berlin":"Germany", "Rio":"Brazil", "Tokyo":"Japan"}

print(S | S2)