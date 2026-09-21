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

def przeliczanieDziesietne(dozmiany):
    dziesietna = 0
    mnozna = 128
    for i in dozmiany:
        if i == 1:
            dziesietna += mnozna
        mnozna /= 2
    return dziesietna

def przeliczanieIpDziesietne(A, B, C, D):
    IpDziesietne = []
    IpDziesietne.append(int(przeliczanieDziesietne(A)))
    IpDziesietne.append(int(przeliczanieDziesietne(B)))
    IpDziesietne.append(int(przeliczanieDziesietne(C)))
    IpDziesietne.append(int(przeliczanieDziesietne(D)))
    return IpDziesietne


def rozdzielanieIp(ip):
    ipRozdzielone = [[],[],[],[]]
    for i in range(4):
        for j in range(8):
            ipRozdzielone[i].append(ip[j + i * 8])
    return ipRozdzielone

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

def PrzeliczanieMaskiBinarne(maska):
    maskaBinarna = []
    for i in range(maska):
        maskaBinarna.append(1)
    for i in range(32 - maska):
        maskaBinarna.append(0)
    return maskaBinarna

def PrzeliczanieAdresuSieci(ip, maska):
    adresSieci = []
    for i in range(32):
        if ip[i] == 1 and maska[i] == 1:
            adresSieci.append(1)
        else:
            adresSieci.append(0)
    return adresSieci

def przeliczanieBroadcastu(adresSieci, maska):
    Broadcast = []
    for i in range(32):
        if adresSieci[i] == 1 or maska[i] == 0:
            Broadcast.append(1)
        else:
            Broadcast.append(0)
    return Broadcast

Abin = przeliczanieBinarne(A)
Bbin = przeliczanieBinarne(B)
Cbin = przeliczanieBinarne(C)
Dbin = przeliczanieBinarne(D)

ipv4 = laczenieIp(Abin, Bbin, Cbin, Dbin)

maskaBinarna = PrzeliczanieMaskiBinarne(maska)
maskaBinarnaRozdzielona = rozdzielanieIp(maskaBinarna)
maskaDziesietna = przeliczanieIpDziesietne(maskaBinarnaRozdzielona[0], maskaBinarnaRozdzielona[1], maskaBinarnaRozdzielona[2], maskaBinarnaRozdzielona[3])

adresSieciBinarny = PrzeliczanieAdresuSieci(ipv4, maskaBinarna)
adresSieciBinarnyRozdzielony = rozdzielanieIp(adresSieciBinarny)
adresSieciDziesiatkowy = przeliczanieIpDziesietne(adresSieciBinarnyRozdzielony[0], adresSieciBinarnyRozdzielony[1], adresSieciBinarnyRozdzielony[2], adresSieciBinarnyRozdzielony[3])

BroadcastBinarny = przeliczanieBroadcastu(adresSieciBinarny, maskaBinarna)
BroadcastBinarnyRozdzielony = rozdzielanieIp(BroadcastBinarny)
BroadcastDziesiatkowy = przeliczanieIpDziesietne(BroadcastBinarnyRozdzielony[0], BroadcastBinarnyRozdzielony[1], BroadcastBinarnyRozdzielony[2], BroadcastBinarnyRozdzielony[3])

# Wypisywanie odpowiedzi
if miesiacUrodzenia < 10:
    print(f"Data Urodzenia: {dzienUrodzenia}.0{miesiacUrodzenia}")
else:
    print(f"Data Urodzenia: {dzienUrodzenia}.{miesiacUrodzenia}")
print("Adres IP:", end=" ")
wypisywanieIpNieBinarne(A, B, C, D)
print(f"Maska CIDR: /{maska}")
print("Maska dziesiętna:", end=" ")
wypisywanieIpNieBinarne(maskaDziesietna[0], maskaDziesietna[1], maskaDziesietna[2], maskaDziesietna[3])
print("Adres sieci:", end=" ")
wypisywanieIpNieBinarne(adresSieciDziesiatkowy[0], adresSieciDziesiatkowy[1], adresSieciDziesiatkowy[2], adresSieciDziesiatkowy[3])
print("Broadcast:", end=" ")
wypisywanieIpNieBinarne(BroadcastDziesiatkowy[0], BroadcastDziesiatkowy[1], BroadcastDziesiatkowy[2], BroadcastDziesiatkowy[3],)