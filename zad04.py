students: list[tuple[str, float, str]] = [("Albert", 4.0,"CWL1"), 
            ("Barbra", 5.0, "CWL1"), 
            ("Cole", 3.0, "CWL1"), 
            ("Dick", 4.0, "CWL2"), 
            ("Elle", 2.0, "CWL2"), 
            ("Freddie", 3.5, "CWL2"), 
            ("Gloria", 5.0, "CWL3"), 
            ("Henry", 2.5, "CWL3"),
            ("Irene", 4.0, "CWL3")]

student_groups:dict[str,list[float]] = {}

#.setdefault(key, value) check whether a value is assigned to the given key and if not assigns the given value to the given key 

for name, grade, group in students:
    student_groups.setdefault(group, []).append(grade)

for group, grades in student_groups.items():
    print(f"{group}: count={len(grades)}, average={round(sum(grades)/len(grades),2)}")

print(f"Groups: {len(student_groups)}")



