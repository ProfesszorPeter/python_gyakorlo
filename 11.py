# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!

a = int(input("Adjon meg egy pozitív egész számot: "))

for i in range(a):
    print(i % 2, end=" ")

print()
