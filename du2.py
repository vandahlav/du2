import csv

#otevření souborů 
with open('prutoky.csv', encoding="utf-8") as csvfile, open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni,\
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

    #cyklus pro procházení souboru
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
            prutok = 0
            zbyle_dny = 0 
            prvniDenVtydnu[5] = f" {vysledek:.4f}"
            writer_7dni.writerow(prvniDenVtydnu)
            print(vysledek) #SMAZAT POTOM
            vysledek = 0
        pocet_dni += 1  
    #výpočet průtoku za zbylé dny
    if pocet_dni % 7 != 6:
        vysledek = prutok / zbyle_dny
        prvniDenVtydnu[5] = f" {vysledek:.4f}"
        print(vysledek)

    #nastavení proměnných pro výpočet ročních průtoků
    rok = 0
    dny_vroce= 0
    citac_roku = 0

    for row in reader:
    #pro roky
        if citac_roku == rok:
            prvniDenVroce = row
        if citac_roku != rok:
            vysledek_2 = rok / dny_vroce
            prvniDenVroce = row
            citac_roku = 0
        dny_vroce = dny_vroce + 1