import csv

with open('prutoky.csv', encoding="utf-8") as csvfile,\
    open("prutoky.csv", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter =",")
    writer = csv.writer(csvoutfile, delimiter =",")  

    citac_prutoku = 0 
    citac_dni = 0 
    vysledek = 0
    prutok = 0

    lines= len(list(reader))    #počet řádků 
    print(lines)

    for row in reader:
        if citac_dni % 7 == 0:
            citac_prutoku = 0
            citac_dni = 0
        



"""
    for row in reader:
        try:
            prutok = float(row[5])
        except ValueError:
            prutok = 0
        finally:
            citac_dni =+ 1
        vysledek = prutok + vysledek
        if citac_dni == 7:
            prutok = float(row[5])
            vysledek = prutok + vysledek
            citac_prutoku = 0
            citac_dni = 0
        if citac_dni % 7 != 0:      
    print(vysledek)
"""
        