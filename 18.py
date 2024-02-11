# Írj egy Python függvényt, amely paraméterként kap 2 egész számot és visszatér
# a két szám által meghatározott zárt intervallumban található egész számok
# összegével! A programodban hívd is meg ezt az alprogramot!


def intervallum(a, b):
    return sum(range(a + 1, b))


a = int(input("Adjon meg egy egész számot: "))
b = int(input("Adjon meg egy másik egész számot: "))

print(intervallum(a, b))
