# Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!

a = int(input("Adja meg a kisebb pozitív valós számot: "))
b = int(input("Adja meg a nagyobbik pozitív valós számot: "))

for i in range(a + 1, b):
    print(i)
