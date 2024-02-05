a = int(input("Adjon meg egy pozitív egész számot: "))

for i in range(a):
    if i < a:
        if i % 3 == 0:
            print(i)
