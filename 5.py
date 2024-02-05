a = float(input("Adja meg az 1. számot: "))
b = float(input("Adja meg az 2. számot: "))
c = float(input("Adja meg az 3. számot: "))

if a + c == b or a + b == c or b + c == a:
    print("a számok közül ha össze adunk kettőt az egyenlő lesz a harmadig számmal")

else:
    print("a számok közül ha össze adunk kettőt az nem lesz egyenlő a harmadik számmal")
