# Írj egy Python programot, amely bekér egy valós (A) és egy egész (K) számot a felhasználótól és kiírja a képernyőre az AK hatvány értékét anélkül, hogy használnád a ** operátort!

A = int(input("Adjon meg egy valós számot: "))
K = int(input("Adjom meg egy egész számot: "))

hatvagyertek = 1

for _ in range(abs(K)):
    hatvagyertek *= A if K > 0 else 1 / A

print(f"{A} szám {K} adig hatványa: {hatvagyertek}")
