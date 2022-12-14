from random import randrange as rr
from string import ascii_lowercase as abeceda

co_sa_robi = input("a = dešifrovať\nb = zašifrovať\n")
fr = open("vstupny_text.txt", "r") #treba zmeniť ak chceme dešifrovať

vysl = ""

def sifrovacka(vstup):
    posun = 2#rr(1,26)
    vysl = ""
    for znak in vstup:
        if znak.islower() and znak.isalpha():
            new = ord(znak) + posun
            if new > 122: new -= 26
            vysl += chr(new)
        else: vysl += znak
    vysl = abeceda[posun-1] + vysl
    return vysl

def desifrovacka(vstup):
    posun = abeceda.index(vstup[0]) +1
    vstup = vstup[1::]
    vysl = ""
    for znak in vstup:
        if znak.islower() and znak.isalpha():
            new = ord(znak) - posun
            if new < 97: new += 26
            vysl += chr(new)
        else: vysl += znak
    return vysl


for line in fr:
    if co_sa_robi == "a": vysl += desifrovacka(line)
    else: vysl += sifrovacka(line)
    
#keby sme chceli aj vypísať > print(vysl)


with open("vystup_24.txt","w") as vysledok:
    vysledok.write("".join(vysl))
