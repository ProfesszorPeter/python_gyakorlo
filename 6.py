a = int(input("Adja meg az 1. egész számot: "))
b = int(input("Adja meg az 2. egész számot: "))
c = int(input("Adja meg az 3. egész számot: "))

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("Mind a 3 szám páros")
else:
    print("valamely szám nem páros")
