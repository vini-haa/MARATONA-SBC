def dif_hora(h1, m1, h2, m2):
    
    h1_in_min = h1 * 60 + m1
    h2_in_min = h2 * 60 + m2

    if h1_in_min < h2_in_min:
        dif = h2_in_min - h1_in_min
    else:
        dif = (24 * 60 - h1_in_min) + h2_in_min 

    return dif 



while True:
    list = map(int, input().split())
    h1, m1, h2, m2 = list

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
        
    print(dif_hora(h1, m1, h2, m2))
