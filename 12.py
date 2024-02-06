# Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!

a = int(input("Adja meg a kisebb pozitív valós számot: "))
b = int(input("Adja meg a nagyobbik pozitív valós számot: "))

if a > b:
    print("nem jó sorrendben adta meg a számokat!")
    quit()
for i in range(a + 1, b):
    print(i)
