import csv

#výpočet sedmideních průtoků - načtení souborů 
with open("vstup.csv", encoding="utf-8") as csvfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni:
    reader = csv.reader(csvfile)
    writer_7dni = csv.writer(csvoutfile_7dni) 

    #nastavení proměnných pro výpočet sedmidenních průtoků 
    pocet_dni = 0 
    prutok = 0
    zbytek = 0
   
    #cyklus pro procházení souboru - výpočet sedmidenních průtoků
    for row in reader:
        zbytek += 1
        #zápis prvního dne v týdnu
        if pocet_dni % 7 == 0:
            prvniDenVtydnu = row
        try:
            prutok += float(row[5])
        except ValueError:
            print("Na řádku", pocet_dni + 1, "jsou chybně zadaná data. Program řádek nebude započítávat.")
        #výpočet průtoku v průběhu týdne 
        if  pocet_dni % 7 == 6:
            vysledek = prutok / 7
            prvniDenVtydnu[5] = f" {vysledek:.4f}"
            writer_7dni.writerow(prvniDenVtydnu)
            prutok = 0
            zbytek = 0 
        pocet_dni += 1
    #výpočet průtoku za zbylé dny
    if (pocet_dni - 1) % 7 != 6:
        vysledek = prutok / (zbytek - 1)
        prvniDenVtydnu[5] = f" {vysledek:.4f}"
        writer_7dni.writerow(prvniDenVtydnu)

#výpočet ročních průtoků - načtení souborů     
with open("vstup.csv", encoding="utf-8") as csvfile,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvfile)
    writer_rok = csv.writer(csvoutfile_rok)

    #nastavení proměnných pro výpočet ročních průtoků
    sumaRadku = 0
    pocitanyRok = 0
    prutok_rok = 0
    rokProPorovnani = 0
    zbyleDny = 1

    #cyklus pro procházení souboru - výpočet ročních průtoků
    for row in reader: 
        rokProPorovnani = int(row[2])
    #nastavení aktuálního počítaného roku
        if sumaRadku == 0:
            pocitanyRok = rokProPorovnani
            prvniDenVroce = row
            minimumProZapis = row
            maximumProZapis = row
            max_prutok = float(row[5])
            min_prutok = float(row[5])
        try:
            prutok_rok += float(row[5])
            posledniPrutok = float(row[5])
        except ValueError:
            print("Na řádku", sumaRadku + 1, "jsou chybně zadaná data. Program řádek nebude započítávat.")
        if pocitanyRok != rokProPorovnani:
            vysledny_prutok = (prutok_rok - posledniPrutok) / (zbyleDny - 1)  #zajištění, aby program počítal včetně posledního dne v roce
            prvniDenVroce[5] = f" {vysledny_prutok:.4f}"
            writer_rok.writerow(prvniDenVroce)
            prutok_rok = 0
            zbyleDny = 1
            pocitanyRok = rokProPorovnani
            prvniDenVroce = row
            prutok_rok = posledniPrutok
        zbyleDny += 1
        sumaRadku += 1

    #výpočet minima a maxima
        if posledniPrutok < min_prutok:
            min_prutok = posledniPrutok
            minimumProZapis = row
        elif posledniPrutok > max_prutok:
            max_prutok = posledniPrutok
            maximumProZapis = row

    #výpočet průtoku pro poslední rok (zbylé dny)
    if pocitanyRok == rokProPorovnani:
        vysledny_prutok = prutok_rok / (zbyleDny - 1)   
        prvniDenVroce[5] = f" {vysledny_prutok:.4f}"
        writer_rok.writerow(prvniDenVroce)

    print(f"Maximální hodnota průtoku nastala dne {maximumProZapis[4]}.{maximumProZapis[3]}.{maximumProZapis[2]} a dosahovala hodnoty: {max_prutok}")
    print(f"Minimální hodnota průtoku nastala dne {minimumProZapis[4]}.{minimumProZapis[3]}.{minimumProZapis[2]} a dosahovala hodnoty: {min_prutok}")