import csv

with open('prutoky.csv', encoding="utf-8") as csvfile,\
    open("prutoky.csv", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter =",")
    writer = csv.writer(csvoutfile, delimiter =",")  
 
    citac_dni = 0 
    vysledek = 0
    prutok = 0
    zbyle_dny = 0

    #lines= len(list(reader))    #počet řádků 
    #print(lines)

    for row in reader:
        zbyle_dny += 1
        if citac_dni % 7 == 0:
            prvniDenVtydnu = row 
            print(prvniDenVtydnu)
        try:
            prutok += float(row[5])
        except ValueError:
            print("Something's wrong.")
        if  citac_dni % 7 == 6:
            vysledek = prutok / 7
            prutok = 0
            zbyle_dny = 0 
            print(vysledek)
            vysledek = 0
        citac_dni += 1  

    if citac_dni % 7 != 6:
        vysledek = prutok / zbyle_dny
        print(vysledek)

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