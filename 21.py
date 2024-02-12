# Írj egy Python eljárást, amely paraméterként kap egy szót (sztringet) és
# annyi darab csillag (*) karaktert ír ki a képernyőre, ahány karaktert
# tartalmazott a szó! A programodban hívd is meg ezt az alprogramot!


def csillagok(a):
    print("*" * a)


a = len(input("Adjon meg egy szót: "))

csillagok(a)
