# Domácí úkol 2 - průměrné sedmidenní a roční průtoky

# Zadání 
Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidenní průměry. Program bude neinteraktivní.

# Zpracování 
Nejprve dojde k načtení vstupních csv souborů, kde jsou takové definovány dva writery (jeden pro týdenní průtoky a druhý pro roční) a reader. Writery slouží pro zápis do výstuprního souboru. Ty jsou dva, tudíž je nutné vytvořit i dva writery. V případě, že program nenajde daný soubor (FileNotFoundError) nebo pokud nemá povolení k vytváření souborů, vypíše chybu. 

Poté jsou inicializovány pomocné proměnné, které je nutné definovat před samotným for cyklem, který prochází vstupní soubor.

Pomocí for cyklu prochází program jednotlivé řádky. Zde jsou do výše definovaných proměnných přiřazeny hodnoty. Nejprve dojde k záposu prvního dne v týdnu, nastaví se aktuální počítaný rok a poté program vypočítá průměrné sedmidenní a roční průtoky. V případě nekorektnosti dat na ně upozorní. Stejně tak pokud budou zadané průtoky záporné či nulové, program na ně upozorní. Pokud zadané hodnoty na průtoku v prvním řádku nepůjdou načíst, program řádek přeskočí a bude počítat až od dalšího. Do výstupních souborů dochází k zápisu vždy v daném if bloku pomocí writeru, přičemž jsou výsledné průměrné průtoky zaokrouhleny na čtyři desetinná místa.

Výpočet maximálního a minimálního průtoku je v rámci téhož for cyklu, kdy pokud je aktuální průtok (tedy posledniPrutok) větší než předešlá hodnota průtoku, přepíše se původní průtok na aktuální a zároveň se do proměnné uloží celý řádek s aktuálním nejvyšším průtokem. Stejný princip platí i pro výpočet minima. Tyto hdonoty jsou následně vypsány do konzole. 

Nakonec dojde k výpočtu průměrných průtoků za zbylé dny se sedmidenním průměrem a s ročním průměrem. Zde není průtok dělen 7 (v případě sedmidenních průtoků), ale zbylými dny.  