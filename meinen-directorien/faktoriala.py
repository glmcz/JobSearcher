def faktorial(n):

    faktorial = 1

    for i in range(n):
        faktorial *= i + 1
    return faktorial

for i in range(10): # it begin from 0 to ..
    print(faktorial(i))
