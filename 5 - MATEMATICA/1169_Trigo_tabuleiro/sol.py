try:
    qntd = int(input())
except ValueError:
    qntd = 0

for _ in range(qntd):
    x = int(input())

    total_graos = (2**x) - 1
    total_kg = total_graos // 12000

    print(f"{total_kg} kg")