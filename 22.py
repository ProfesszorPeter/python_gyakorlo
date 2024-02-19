# Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és
# kiír a képernyőre ennyi karaktert úgy, hogy minden harmadik karakter pluszjel
# (+) legyen a többi viszont mínuszjel (-)! A programodban hívd is meg ezt az alprogramot!


def csere(a):
    for i in range(a):
        if i % 3 == 0:
            print("+", end=" ")
        else:
            print("-", end=" ")


a = int(input("Adjon meg egy pozitív egész számot: "))

csere(a)
