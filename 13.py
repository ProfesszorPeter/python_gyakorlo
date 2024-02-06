# Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak!


a = int(input("Adja meg egy pozitív valós számot: "))
b = int(input("Adja meg egy másik pozitív valós számot: "))

for i in range(a + 1, b):
    if i % 2 == 0:
        print(i)
