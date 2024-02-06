# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege!

a = int(input("Adjon meg egy pozitív egész számot: "))

osszeg = sum(range(1, a + 1))

print(f"Az {a} és ennél kisebb pozitív egész számok összege: {osszeg}")
