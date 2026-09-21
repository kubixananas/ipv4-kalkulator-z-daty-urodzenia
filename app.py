dzienUrodzenia = int(input("Wprowadź dzień urodzenia: "))
miesiacUrodzenia = int(input("Wprowadź miesiąc urodzenia: "))

A = 100 + dzienUrodzenia
B = 200 + miesiacUrodzenia
C = 160 + dzienUrodzenia + miesiacUrodzenia
D = 222 - dzienUrodzenia

maska = 17 + miesiacUrodzenia

def przeliczanieBinarne(dozmiany):
    binarna = []
    dzielna = 128
    while dzielna >= 1:
        if dozmiany >= dzielna:
            binarna.append(1)
            dozmiany -= dzielna
        else:
            binarna.append(0)
        dzielna /= 2
    return binarna
