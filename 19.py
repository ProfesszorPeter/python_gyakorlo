# Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól
# és kiírja a képernyőre, hogy van-e olyan betű, amelyik mind a kettőben előfordul!

a = set(input("Adjon meg egy szót: "))
b = set(input("Adjon meg egy másik szót: "))
c = a.intersection(b)

if c:
    print(f"A közös karakter(ek): {c}")
else:
    print("nincs közös karakter a kettő szóban")
