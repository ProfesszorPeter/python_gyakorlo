# Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!


def teglalap(N, M):
    for i in range(M):
        print("* " * N)


N = int(input("Adja meg az oszlopok számát: "))
M = int(input("Adja meg a sorok számát: "))

teglalap(N, M)
