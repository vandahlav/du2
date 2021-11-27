import csv
try: 
    #načtení a otevření souborů 
    with open("vstup.csv", encoding="utf-8") as csvfile,\
        open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_7dni,\
        open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
        reader = csv.reader(csvfile)
        writer_7dni = csv.writer(csvoutfile_7dni)
        writer_rok = csv.writer(csvoutfile_rok)  

        #nastavení proměnných pro výpočty
        pocet_dni = 0 
        prutok = 0
        prutok_rok = 0
        zbyleDnyVroce = 0 
        zbyleDny = 1
    
        #cyklus pro procházení souboru
        for row in reader:
            zbyleDnyVroce += 1
            rokProPorovnani = int(row[2])

            #zápis prvního dne v týdnu
            if pocet_dni % 7 == 0:
                prvniDenVtydnu = row

            #nastavení aktuálního počítaného roku
            if pocet_dni == 0:
                pocitanyRok = rokProPorovnani
                prvniDenVroce = row
                minimumProZapis = row
                maximumProZapis = row
                max_prutok = float(row[5])
                min_prutok = float(row[5])
            try:
                prutok += float(row[5])
                prutok_rok += float(row[5])
                posledniPrutok = float(row[5])
            except ValueError:
                print("Na řádku", pocet_dni + 1, "jsou chybně zadaná data. Program řádek nebude započítávat.")

            #upozornění na chyby ve vstupních datech
            if posledniPrutok == 0:
                print(f"Na řádku {pocet_dni + 1} je nulová hodnota průtoku.")
            elif posledniPrutok < 0:
                print(f"Na řádku {pocet_dni + 1} jsou záporné hodnoty průtoku. Hodnota průtoku je: {posledniPrutok}")

            #výpočet průtoku v průběhu týdne 
            if  pocet_dni % 7 == 6:
                vysledek = prutok / 7
                prvniDenVtydnu[5] = f" {vysledek:.4f}"
                writer_7dni.writerow(prvniDenVtydnu)
                prutok = 0
                zbyleDnyVroce = 0 
            pocet_dni += 1

            #výpočet ročních průtoků
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

        #výpočet minima a maxima
            if posledniPrutok < min_prutok and posledniPrutok > 0:
                minimumProZapis = row
                min_prutok = posledniPrutok
            elif posledniPrutok > max_prutok:
                max_prutok = posledniPrutok
                maximumProZapis = row

        #výpočet průtoku za zbylé dny
        if (pocet_dni - 1) % 7 != 6:   
            vysledek = prutok / zbyleDnyVroce
            prvniDenVtydnu[5] = f" {vysledek:.4f}"
            writer_7dni.writerow(prvniDenVtydnu)

        #výpočet průtoku pro poslední rok (zbylé dny)
        if pocitanyRok == rokProPorovnani:
            vysledny_prutok = prutok_rok / (zbyleDny - 1)   
            prvniDenVroce[5] = f" {vysledny_prutok:.4f}"
            writer_rok.writerow(prvniDenVroce)

    print(f"Maximální hodnota průtoku nastala dne {maximumProZapis[4]}.{maximumProZapis[3]}.{maximumProZapis[2]} a dosahovala hodnoty: {max_prutok}")
    print(f"Minimální hodnota průtoku nastala dne {minimumProZapis[4]}.{minimumProZapis[3]}.{minimumProZapis[2]} a dosahovala hodnoty: {min_prutok}")

except FileNotFoundError:
    print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta")