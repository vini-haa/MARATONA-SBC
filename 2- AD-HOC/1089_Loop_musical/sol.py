def contar_picos(amostras):
    n = len(amostras)
    picos = 0

    for i in range(n):
        ant = amostras[i - 1]
        atual = amostras[i]
        prox = amostras[(i + 1) % n]

        if (atual > ant and atual > prox) or (atual < ant and atual < prox):
            picos += 1

    return picos

while True:
    n = int(input())

    if n == 0:
        break

    amostras = list(map(int, input().split()))
    print(contar_picos(amostras))
