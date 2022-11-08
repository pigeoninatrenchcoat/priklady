fr_a = open("hlasovanie_2.txt", "r")
fr_b = open("hlasovanie_vypadnuti.txt", "r")

kolko = 0

hlasy = {}
for i in range(5220,5230):
    hlasy[i] = 0

vypadnuti = []
for h in fr_b:
    vypadnuti.append(h.strip())

for hlas in fr_a:
    kolko += 1
    hlasy[int(hlas.strip())] += 1

print(f"Hlasov bolo odoslaných {kolko}.")

for i in hlasy:
    print(f"Číslo {i} dostalo {hlasy[i]} hlasov.")

print(f"Suverénne najmenej hlasov dostalo číslo {min(hlasy, key = hlasy.get)}. ")

for f in vypadnuti: hlasy.pop(int(f))

print(f"Vypadáva {min(hlasy, key = hlasy.get)}.")
