import sys

def fatorial(num):
    if num == 0:
        return 1

    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado


while True:
    try: 
        linha = sys.stdin.readline()
        if not linha: 
            break
    
        M, N = map(int, linha.split())

        soma = fatorial(M) + fatorial(N)
        print(soma)

    except EOFError:
        break
