def vypocitej_faktorial():
    k = 10
    while k>0:
        n = int(input())
        fact = 1

        for i in range(1, n+1):
            fact = fact * i

        print("Výsledek je: ", end="")
        print(fact)
        k -= 1
