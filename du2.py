import csv

#výpočet sedmideních průtoků - načtení souborů 
with open("Peti_vstup_du2.csv", encoding="utf-8") as csvfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni:
    reader = csv.reader(csvfile)
    writer_7dni = csv.writer(csvoutfile_7dni) 

    #nastavení proměnných pro výpočet sedmidenních průtoků 
    pocet_dni = 0 
    vysledek = 0
    prutok = 0
    zbytek = 0

    #lines= len(list(reader))    #počet řádků 
    #print(lines)
    
    #cyklus pro procházení souboru - výpočet sedmidenních průtoků
    for row in reader:
        zbytek += 1
        #zápis prvního dne v týdnu
        if pocet_dni % 7 == 0:
            prvniDenVtydnu = row 
        try:
            prutok += float(row[5])
        except ValueError:
            print("Something's wrong.")
        #výpočet průtoku v průběhu týdne 
        if  pocet_dni % 7 == 6:
            vysledek = prutok / 7
            prvniDenVtydnu[5] = f" {vysledek:.4f}"
            writer_7dni.writerow(prvniDenVtydnu)
            prutok = 0
            zbytek = 0 
            vysledek = 0
        pocet_dni += 1 
    #výpočet průtoku za zbylé dny
    if pocet_dni % 7 != 6:
        vysledek = prutok / zbytek
        prvniDenVtydnu[5] = f" {vysledek:.4f}"

#výpočet ročních průtoků - načtení souborů     
with open("Peti_vstup_du2.csv", encoding="utf-8") as csvfile,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvfile)
    writer_rok = csv.writer(csvoutfile_rok)

    #nastavení proměnných pro výpočet ročních průtoků
    prvniRadek = 0
    pocetRoku = 0
    pocitanyRok = 0
    prutok_rok = 0
    aktualizovanyRok = 0
    zbyleDny = 0
    posledniDen = 0

    #cyklus pro procházení souboru - výpočet ročních průtoků
    for row in reader: 
        aktualizovanyRok = int(row[2])
        #nastavení aktuálního počítaného roku
        if prvniRadek == 0:
            pocitanyRok == aktualizovanyRok
            prvniDenVroce = row
        try:
            prutok_rok += float(row[5])
        except ValueError:
            print("Something's wrong.")
        posledniDen = float(row[5])
        if pocitanyRok != aktualizovanyRok:
            vysledek_rok = (prutok_rok  - posledniDen) / (zbyleDny - 1)  #zajištění, aby program počítal poslední den (tedy včetně něj)
            print(aktualizovanyRok, vysledek_rok)
            prutok_rok = 0
            vysledek_rok = 0
            zbyleDny = 0
            pocitanyRok = aktualizovanyRok
            prvniDenVroce = row
        zbyleDny += 1
print("All done.")