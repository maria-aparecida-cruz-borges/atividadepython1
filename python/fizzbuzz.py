print("Diga-me um número: ")
numero = int (input())

if numero % 15 == 0:
    print("fizzbuzz")
elif numero % 3 == 0:
    print("fizz")
elif numero % 5 == 0:
    print("buzz")
else:
    print(numero)

