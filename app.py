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

def wypisywanieIpBinarne(ip):
    for i in range(32):
        print(ip[i], end="")
        if i == 7 or i == 15 or i == 23:
            print(".", end="")
    print("")

def wypisywanieIpNieBinarne(A, B, C, D):
    print(A, end="")
    print(".", end="")
    print(B, end="")
    print(".", end="")
    print(C, end="")
    print(".", end="")
    print(D)

def laczenieIp(A, B, C, D):
    ip = []
    for i in A:
        ip.append(i)
    for i in B:
        ip.append(i)
    for i in C:
        ip.append(i)
    for i in D:
        ip.append(i)
    return ip

Abin = przeliczanieBinarne(A)
Bbin = przeliczanieBinarne(B)
Cbin = przeliczanieBinarne(C)
Dbin = przeliczanieBinarne(D)

ipv4 = laczenieIp(Abin, Bbin, Cbin, Dbin)

# Wypisywanie odpowiedzi
if miesiacUrodzenia < 10:
    print(f"Data Urodzenia: {dzienUrodzenia}.0{miesiacUrodzenia}")
else:
    print(f"Data Urodzenia: {dzienUrodzenia}.{miesiacUrodzenia}")
print("Adres IP:", end=" ")
wypisywanieIpNieBinarne(A, B, C, D)