import csv

#výpočet sedmideních průtoků - načtení souborů 
with open("prutoky.csv", encoding="utf-8") as csvfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni:
    reader = csv.reader(csvfile)
    writer_7dni = csv.writer(csvoutfile_7dni) 

    #nastavení proměnných pro výpočet sedmidenních průtoků 
    pocet_dni = 0 
    vysledek = 0
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
        except IndexError:
            print("první except - mám jen jeden týden")
        except ValueError:
            print("Na řádku", pocet_dni + 1, "jsou chybně zadaná data. Program řádek nebude započítávat.")
        except:
            print("Záporná hodnota průtoku na řádku", pocet_dni + 1) 
        #výpočet průtoku v průběhu týdne 
        if  pocet_dni % 7 == 6:
            vysledek = prutok / 7
            prvniDenVtydnu[5] = f" {vysledek:.4f}"
            print("Průměrný sedmidenní průtok je", f" {vysledek:.4f}")
            writer_7dni.writerow(prvniDenVtydnu)
            prutok = 0
            zbytek = 0 
            vysledek = 0
        pocet_dni += 1
    #výpočet průtoku za zbylé dny
    if pocet_dni % 7 != 6:
        vysledek = prutok / zbytek
        """NEFUNGUJE JEN NA JEDEN TÝDEN - NĚJAK SPRAVIT"""
        prvniDenVtydnu[5] = f" {vysledek:.4f}"
        print("Průměrný sedmidenní průtok je", f" {vysledek:.4f}")
        writer_7dni.writerow(prvniDenVtydnu)

#výpočet ročních průtoků - načtení souborů     
with open("prutoky.csv", encoding="utf-8") as csvfile,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvfile)
    writer_rok = csv.writer(csvoutfile_rok)

    #nastavení proměnných pro výpočet ročních průtoků
    sumaRadku = 0
    pocitanyRok = 0
    prutok_rok = 0
    rokProPorovnani = 0
    zbyleDny = 1
    min_prutok = 0
    max_prutok = 0

    #cyklus pro procházení souboru - výpočet ročních průtoků
    for row in reader: 
        rokProPorovnani = int(row[2])
        #nastavení aktuálního počítaného roku
        if sumaRadku == 0:
            pocitanyRok = rokProPorovnani
            prvniDenVroce = row
        try:
            prutok_rok += float(row[5])
            posledniPrutok = float(row[5])
        except ValueError:
            print("Na řádku", sumaRadku + 1, "jsou chybně zadaná data. Program řádek nebude započítávat.")
        if pocitanyRok != rokProPorovnani:
            vysledny_prutok = (prutok_rok - posledniPrutok) / (zbyleDny - 1)  #zajištění, aby program počítal včetně posledního dne v roce
            prvniDenVroce[5] = f" {vysledny_prutok:.4f}"
            writer_rok.writerow(prvniDenVroce)
            print("Pro rok", pocitanyRok, "je průměrný průtok", f" {vysledny_prutok:.4f}")
            prutok_rok = 0
            zbyleDny = 1
            pocitanyRok = rokProPorovnani
            prvniDenVroce = row
            prutok_rok = posledniPrutok
        zbyleDny += 1
        sumaRadku += 1
        #posledniPrutok = min_prutok

        """#výpočet minima a maxima 
        print("posledni prutok", posledniPrutok)
        if posledniPrutok < min_prutok and sumaRadku > 0:
            min_prutok = row
        elif posledniPrutok > max_prutok:
            max_prutok = row
        print("max:",max_prutok, "min:", min_prutok)"""

    #výpočet průtoku pro poslední rok (zbylé dny)
    if pocitanyRok == rokProPorovnani:
        vysledny_prutok = prutok_rok / (zbyleDny - 1)   
        prvniDenVroce[5] = f" {vysledny_prutok:.4f}"
        writer_rok.writerow(prvniDenVroce)
        print("Pro rok", pocitanyRok, "je průměrný průtok",f" {vysledny_prutok:.4f}")

    