from collections import deque

d: deque[int] = deque[int]([1,2,3,4,5])

print(list(d))

d.append(6)

print("Dodano element z prawej", list(d))

d.appendleft(0)

print("Dodano element z lewej", list(d))

fifo_que : deque[int] = deque[int]([1,2,3,4])

lifo_stack : list[int] = [1,2,3,4]

elements: list[int] = [5,6,7,8,9]
for element in elements:
    fifo_que.append(element)
    print(f"Dodano  do kolejki: {element}")

while fifo_que:
    deleted_element = fifo_que.popleft()
    print(f"Usunieto: {deleted_element}")

for element in elements:
    lifo_stack.append(element)
    print(f"Dodano do stosu: {element}")
while lifo_stack:
    deleted_element = lifo_stack.pop()
    print(f"Usunieto {deleted_element}")

    





