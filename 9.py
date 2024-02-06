# Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!

a = int(input("Adjon megy egy 20-nál nem nagyobb pozitív egész számot: "))

for _ in range(a):
    print(" ", end="")

print("START")
