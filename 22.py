from random import shuffle

fr = open("poprehadzovany_text_vstup2.txt", "r")

vysl = []

def pomiesaj(ehe):
    ehe = "".join(ehe)
    h = list(ehe[1:len(ehe)-1:])
    shuffle(h)
    ehe = ehe[:1:] + "".join(h) + ehe[len(ehe)-1::]
    return ehe


for line in fr:
    temp = []
    line = line.strip().split(" ")
    for slovo in line:
        koniec, kolko, ehe = "", 0, list(slovo)
        for pis in slovo:
            if pis.isalpha():
                koniec += "_"
                kolko += 1
            else:
                koniec += pis
                ehe.remove(pis)
        koniec = koniec.replace("_"*kolko, "_")
        ehe = pomiesaj(ehe)
        temp.append(koniec.replace("_", ehe))
    temp = " ".join(temp)
    vysl.append(temp + "\n")

print("".join(vysl))
#vypis do suboru, funkcia pomiesaj


with open("poprehadzovany_text.txt","w") as vysledok:
    vysledok.write("".join(vysl))
