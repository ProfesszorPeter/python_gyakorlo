# Írj egy Python eljárást, amely paraméterként kap egy egész számot és kiírja a
# képernyőre az ennél kisebb értékű elemeit a Fibonacci sornak!


# mi-vel oldottam meg...
def fibonacci(N):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] < N:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print("Az ennél kisebb Fibonacci számok:")
    for elem in fibonacci:
        print(elem, end=" ")


N = int(input("Adja meg meg a fibonacci számok számok felső határát: "))

fibonacci(N)
