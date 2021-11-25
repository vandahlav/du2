import csv

#otevření souborů 
with open("prutoky.csv", encoding="utf-8") as csvfile, open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvfile)
    writer_7dni = csv.writer(csvoutfile_7dni)
    writer_rok = csv.writer(csvoutfile_rok)  

    #nastavení proměnných pro výpočet sedmidenních průtoků 
    pocet_dni = 0 
    vysledek = 0
    prutok = 0
    zbyle_dny = 0

    #lines= len(list(reader))    #počet řádků 
    #print(lines)
    """
    #cyklus pro procházení souboru - výpočet sedmidenních průtoků
    for row in reader:
        zbyle_dny += 1
        #zápis prvního dne v týdnu
        if pocet_dni % 7 == 0:
            prvniDenVtydnu = row 
            print(prvniDenVtydnu)
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
            zbyle_dny = 0 
            vysledek = 0
        pocet_dni += 1 
    #výpočet průtoku za zbylé dny
    if pocet_dni % 7 != 6:
        vysledek = prutok / zbyle_dny
        prvniDenVtydnu[5] = f" {vysledek:.4f}"
    """
    #nastavení proměnných pro výpočet ročních průtoků
    prvniRadek = 0
    pocetRoku = 0
    pocitanyRok = 0
    prutok_rok = 0
    aktualizovanyRok = 0
    zbytek = 0

    #cyklus pro procházení souboru - výpočet ročních průtoků
    for row in reader: 
        aktualizovanyRok = int(row[2]) 
        if prvniRadek == 0:
            pocitanyRok == aktualizovanyRok
            prvniDenVroce = row
        try:
            prutok_rok += float(row[5])
        except ValueError:
            print("Something's wrong.")
        zbytek += 1
        if pocitanyRok != aktualizovanyRok:
            vysledek_rok = (prutok_rok) / (zbytek)
            print(aktualizovanyRok, vysledek_rok)
            prutok_rok = 0
            vysledek_rok = 0
            zbytek = 0
            pocitanyRok = aktualizovanyRok
            prvniDenVroce = row