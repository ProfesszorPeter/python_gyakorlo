# Írj egy Python programot, amely bekér a felhasználótól egy sztringet és ezt
# úgy íratja ki, hogy a szóköz karaktereket kihagyja!


def szunetmentes(szoveg):
    szavak = szoveg.split()
    for i in szavak:
        print(i, end="")


a = input("Adjon meg egy szöveget: ")

szunetmentes(a)
