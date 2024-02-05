x = float(input("Adja meg a dolgozat pontszámát: "))

if x < 50:
    erdemjegy = 1

elif 50 <= x < 60:
    erdemjegy = 2

elif 60 <= x < 70:
    erdemjegy = 3

elif 70 <= x < 85:
    erdemjegy = 4

else:
    erdemjegy = 5

print(f"Az érdemjegy: {erdemjegy}")
