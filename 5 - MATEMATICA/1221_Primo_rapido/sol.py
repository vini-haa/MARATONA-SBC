def primo(num):
    if num < 2:
        return False
    
    if num == 2:
        return True

    if num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    
    limite = int(num**0.5) + 1

    for i in range (3, limite, 2):
        if num % i == 0:
            return False
    return True

    

qntd = int(input())

for _ in range(qntd):
    num = int(input())
    primo_num = primo(num)
    if primo_num:
        print("Prime")
    else:
        print("Not Prime")

