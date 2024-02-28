# Írj egy Python programot, amely bekér a felhasználótól egy mondatot
# (sztringet) és ennek szavait (szóközzel elválasztott részsztringjeit)
# fordított sorrendben kiírja a képernyőre!


def forditott_sorrend(szoveg):
    szavak = szoveg.split()
    szaval_vissza = szavak[::-1]

    for i in szaval_vissza:
        print(i)


mondat = input("Adjon meg egy mondatot: ")

forditott_sorrend(mondat)
