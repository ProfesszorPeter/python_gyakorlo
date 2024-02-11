# Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap
# három számot és eldönti, hogy az összes paramétere pozitív-e! A programodban
# hívd is meg ezt az alprogramot!


def pizitiv(a, b, c):
    return a > 0 and b > 0 and c > 0


a = int(input("Adja meg az első pozitív számot: "))
b = int(input("Adja meg a második pozitív számot: "))
c = int(input("Adja meg a harmadik pozitív számot: "))


print(pizitiv(a, b, c))
