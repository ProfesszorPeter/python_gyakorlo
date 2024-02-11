# Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap
# egy egész számot és  eldönti a számról, hogy osztható-e 2-vel és 3-mal is
# egyszerre! A programodban hívd is meg ezt az alprogramot!


def oszthasosag(szam):
    return szam % 2 == 0 and szam % 3 == 0


a = int(input("Adjon meg egy egész számot: "))


print(oszthasosag(a))
