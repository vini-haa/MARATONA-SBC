while True:
    B, N = map(int, input().split())

    if B == 0 and N == 0:
        break

    reservas = list(map(int, input().split()))
    reservas.insert(0,0)

    for _ in range(N):
        D, C, V = map(int, input().split())
        reservas[D] -= V
        reservas[C] += V

    possivel = all(r >= 0 for r in reservas[1:])

    print('S' if possivel else 'N')