import random
import sys
print("Mitä halua tehdä? Jos haluat avata tallennetun pelin, kirjoita valinta -kohtaan A. Jos haluat aloittaa uuden pelin, valitse B.")
def pääsikö_jatkoon():
    """
    Funktio tarkistaa, pääsikö käyttäjä jatkoon
    """
    if kertolaskupisteet >= 4: 
        print("Pääsit jatkoon!")
    else:
        print("Putosit!")
        sys.exit()
def voittiko_kayttaja():
    """
    Tämä funktio tarkistaa, onko käyttäjä voittanut pelin
    """
    if eteneminen  >= 3:
        print("Voitit pelin!")
        sys.exit()
valinta = input("Valitse: ")
def avaa_peli(nimi:str):  
        """
        Tämä funktio avaa tallennetun pelin
        """
        with open("ksp"+str(nimi)+".txt","r") as tiedosto:
            sisalto = tiedosto.read()
            eteneminen = int(sisalto)
            print("Peli alkaa tasosta yksi(kivi, sakset, paperi -peli), mutta edistymispisteesi on tallennettu. Aloita valitsemalla joko kivi, paperi tai sakset. Muista kirjoittaa valintasi pienellä alkukirjaimella.")
            print("Edistymisesi: ",eteneminen,"piste(ttä)")
        vaihtoehdot = ["kivi","paperi","sakset"]
        erat = 1
        p1erat = 0
        p2erat = 0
        while erat <= 5:
            while erat <= 5:
                try:
                    p1valinta = input("Valitse: ")
                    p2valinta = random.choice(vaihtoehdot)
                    if p1valinta == "kivi" and p2valinta == "sakset":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == "sakset"  and p2valinta == "paperi":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == "paperi" and p2valinta == "kivi":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == p2valinta:
                        print("Tasapeli!")
                    if p1valinta == "kivi" and p2valinta == "paperi":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == "paperi" and p2valinta == "sakset":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == "sakset" and p2valinta == "kivi":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == p1valinta.capitalize():
                        print("Kirjoita valinta pienellä alkukirjaimella!")
                    elif p1valinta not in vaihtoehdot:
                            print("Syötä joko kivi, paperi tai sakset!")
                except ValueError:
                    print("Syötä joko kivi, paperi tai sakset!")
                erat += 1
        if p1erat > p2erat:
            print("Pääsit jatkoon")
            eteneminen += 1
        else:
            putosit()
        print("Edistymisesi:",eteneminen,"piste(ttä)")
        def voittiko_kayttaja():
                if eteneminen  >= 3:
                    print("Voitit pelin!")
                    sys.exit()
                else:
                    pass
        voittiko_kayttaja()
        print("Haluatko tallentaa? Jos haluat, kirjoita valintaan kyllä. Jos haluat jatkaa, kirjoita ei.")
        valinta = input("Valitse: ")
        if valinta == "kyllä":
            def tallenna_peli(nimi:str):
                with open("ksp"+str(nimi)+".txt","w") as tiedosto:
                    tiedosto.write(str(eteneminen))
                    tiedosto.close()
                    sys.exit()  
            nimi = input("Anna tallenteen nimi: ")
            tallenna_peli(nimi)
        elif valinta == "ei":
            print("Kierros numero 2")
            laskuerat = 1
            numerot = [0,1,2,3,4,5,6,7,8,9,10]
            kertolaskupisteet = 0
            def voittiko_kayttaja():
                if eteneminen  >= 3:
                    print("Voitit pelin!")
                    sys.exit()
            voittiko_kayttaja()
            while laskuerat <= 5:
                try:
                    numero1 = random.choice(numerot)

                    numero2 = random.choice(numerot)

                    kertolasku = numero1,"*",numero2
                    print(kertolasku)
                    vastaus = int(input("Anna vastaus: "))
                    oikea_vastaus = numero1 * numero2
                    if(vastaus == oikea_vastaus):
                        kertolaskupisteet += 1
                        print("Oikein!")
                    else:
                        print("Väärin!")
                except ValueError:
                    print("Anna vastaus kokonaislukuina!")
                laskuerat +=1
            def pääsikö_jatkoon():
                if kertolaskupisteet >= 4: 
                    print("Pääsit jatkoon!")
                else:
                    print("Putosit!")
                    sys.exit()
            eteneminen += 1
            def tallenna_peli(nimi:str):
                with open("ksp"+str(nimi)+".txt","w") as tiedosto:
                    tiedosto.write(str(eteneminen))
                    tiedosto.close()
                    sys.exit()  
            print("Edistymisesi: ",eteneminen,"piste(ttä)")
            voittiko_kayttaja()
            pääsikö_jatkoon()
            print("Haluatko tallentaa? Jos haluat, kirjoita valintaan kyllä. Jos haluat jatkaa, kirjoita ei.")
            valinta = input("Valitse: ")
            if valinta == "kyllä":
                nimi = input("Anna tallenteen nimi: ")
                tallenna_peli(nimi)
            elif valinta == "ei":
                print("Nyt pelataan vielä toinen kierros kps:ää. Jos voitat tämän erän, voitat koko pelin. Muista kirjoittaa valintasi pienellä alkukirjaimella")
                erat = 1
                p1erat = 0
                p2erat = 0
                voittiko_kayttaja()
                while erat <= 5:
                    try:
                        p1valinta = input("Valitse: ")
                        p2valinta = random.choice(vaihtoehdot)
                        if p1valinta == "kivi" and p2valinta == "sakset":
                            p1erat += 1
                            print("Sait yhden erävoiton!")
                        elif p1valinta == "sakset"  and p2valinta == "paperi":
                            p1erat += 1
                            print("Sait yhden erävoiton!")
                        elif p1valinta == "paperi" and p2valinta == "kivi":
                            p1erat += 1
                            print("Sait yhden erävoiton!")
                        elif p1valinta == p2valinta:
                            print("Tasapeli!")
                        if p1valinta == "kivi" and p2valinta == "paperi":
                            print("Vastustaja voitti tämän erän!")
                            p2erat += 1
                        elif p1valinta == "paperi" and p2valinta == "sakset":
                            print("Vastustaja voitti tämän erän!")
                            p2erat += 1
                        elif p1valinta == "sakset" and p2valinta == "kivi":
                            print("Vastustaja voitti tämän erän!")
                            p2erat += 1
                        elif p1valinta == p1valinta.capitalize():
                            print("Kirjoita valinta pienellä alkukirjaimella!")
                        elif p1valinta not in vaihtoehdot:
                            print("Syötä joko kivi, paperi tai sakset!")
                    except ValueError:
                        print("Syötä joko kivi, paperi tai sakset!")
                    erat += 1
                print("Edistymisesi: ",eteneminen,"piste(ttä)")
                voittiko_kayttaja()
                valinta=input("Haluatko tallentaa? Vastaa kyllä tai ei")
                if valinta == "kyllä":
                    if p1erat>p2erat:
                        eteneminen += 1
                        nimi = input("Anna tallenteen nimi: ")
                        tallenna_peli(nimi)
                    elif valinta == "ei":
                        if p1erat>p2erat:
                            eteneminen += 1
                            voittiko_kayttaja()
                        else:
                            print("Hävisit ja peli päättyi!")
                    else: 
                        print("Syötä joko kyllä tai ei")
            else:
                print("Syötä joko kyllä tai ei")
            sys.exit()
def tallenna_peli(nimi:str):
    """
    Tämä funktio tallentaa pelin.
    """
    with open("ksp"+str(nimi)+".txt","w") as tiedosto:
        tiedosto.write(str(eteneminen))
        tiedosto.close()
        sys.exit()  
def putosit():
    """
    käyttäjä pudotetaan jatkosta tällä funktiolla
    """
    print("Putosit jatkosta!")
    sys.exit()
def pääsikö_jatkoon():
    """
    Tarkistaa, pääsikö käyttäjä jatkoon
    """
    if kertolaskupisteet >= 4: 
        print("Pääsit jatkoon!")
    else:
        print("Putosit!")
        sys.exit()
def voittiko_kayttaja():
    """
    Tämä funktio tarkistaa, onko käyttäjä voittanut pelin
    """
    if eteneminen  >= 3:
        print("Voitit pelin!")
eteneminen = 0
try:
    if valinta == "A":
        try:
            nimi = input("Anna tallenteen nimi: ")
            avaa_peli(nimi)
        except FileNotFoundError:
            print("Väärä tiedostonimi. Yritä uudestaan käynnistämällä ohjelma uudelleen")

    elif valinta == "B":
        print(f"Tervetuloa pelaamaan ksp & kertolasku -peliä! Muista kirjoittaa valintasi pienellä alkukirjaimella.")
        vaihtoehdot = ["kivi","paperi","sakset"]
        erat = 1
        p1erat = 0
        p2erat = 0
        while erat <= 5:
            try:
                p1valinta = input("Valitse: ")
                p2valinta = random.choice(vaihtoehdot)
                if p1valinta == "kivi" and p2valinta == "sakset":
                    p1erat += 1
                    print("Sait yhden erävoiton!")
                elif p1valinta == "sakset"  and p2valinta == "paperi":
                    p1erat += 1
                    print("Sait yhden erävoiton!")
                elif p1valinta == "paperi" and p2valinta == "kivi":
                    p1erat += 1
                    print("Sait yhden erävoiton!")
                elif p1valinta == p2valinta:
                    print("Tasapeli!")
                if p1valinta == "kivi" and p2valinta == "paperi":
                    print("Vastustaja voitti tämän erän!")
                    p2erat += 1
                elif p1valinta == "paperi" and p2valinta == "sakset":
                    print("Vastustaja voitti tämän erän!")
                    p2erat += 1
                elif p1valinta == "sakset" and p2valinta == "kivi":
                    print("Vastustaja voitti tämän erän!")
                    p2erat += 1
                elif p1valinta == p1valinta.capitalize():
                    print("Kirjoita valinta pienellä alkukirjaimella!")
                elif p1valinta not in vaihtoehdot:
                            print("Syötä joko kivi, paperi tai sakset!")
            except ValueError:
                print("Syötä joko kivi, paperi tai sakset!")
            erat += 1
        if p1erat > p2erat:
            print("Pääsit jatkoon")
            eteneminen += 1
        else:
            putosit()
        print("Edistymisesi:",eteneminen,"piste(ttä)")
        print("Haluatko tallentaa? Jos haluat, kirjoita valintaan kyllä. Jos haluat jatkaa, kirjoita ei.")
        valinta = input("Valitse: ")
        if valinta == "kyllä":
            nimi = input("Anna tallenteen nimi: ")
            tallenna_peli(nimi)
        elif valinta == "ei":
            print("Kierros numero 2")
            laskuerat = 1
            numerot = [0,1,2,3,4,5,6,7,8,9,10]
            kertolaskupisteet = 0
            voittiko_kayttaja()
            while laskuerat <= 5:
                try:
                    numero1 = random.choice(numerot)

                    numero2 = random.choice(numerot)

                    kertolasku = numero1,"*",numero2
                    print(kertolasku)
                    vastaus = int(input("Anna vastaus: "))
                    oikea_vastaus = numero1 * numero2
                    if(vastaus == oikea_vastaus):
                        kertolaskupisteet += 1
                        print("Oikein!")
                    else:
                        print("Väärin!")
                except ValueError:
                    print("Anna vastaus kokonaislukuna!")
                laskuerat += 1
        pääsikö_jatkoon()
        eteneminen += 1
        print("Edistymisesi: ",eteneminen,"piste(ttä")
        print("Haluatko tallentaa? Jos haluat, kirjoita valintaan kyllä. Jos haluat jatkaa, kirjoita ei. Muista kirjoittaa valintasi pienellä alkukirjaimella.")
        valinta = input("Valitse: ")
        if valinta == "kyllä":
            nimi = input("Anna tallenteen nimi: ")
            tallenna_peli(nimi)
        elif valinta == "ei":
            print("Nyt pelataan vielä toinen kierros kps:ää. Jos voitat tämän erän etkä halua tallentaa, voitat koko pelin.")
            erat = 1
            p1erat = 0
            p2erat = 0
            while erat <= 5:
                try:
                    p1valinta = input("Valitse: ")
                    p2valinta = random.choice(vaihtoehdot)
                    if p1valinta == "kivi" and p2valinta == "sakset":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == "sakset"  and p2valinta == "paperi":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == "paperi" and p2valinta == "kivi":
                        p1erat += 1
                        print("Sait yhden erävoiton!")
                    elif p1valinta == p2valinta:
                        print("Tasapeli!")
                    if p1valinta == "kivi" and p2valinta == "paperi":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == "paperi" and p2valinta == "sakset":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == "sakset" and p2valinta == "kivi":
                        print("Vastustaja voitti tämän erän!")
                        p2erat += 1
                    elif p1valinta == p1valinta.capitalize():
                        print("Kirjoita valinta pienellä alkukirjaimella!")
                    elif p1valinta not in vaihtoehdot:
                            print("Syötä joko kivi, paperi tai sakset!")
                except ValueError:
                    print("Syötä joko kivi, paperi tai sakset!")
                erat += 1
            print("Haluatko tallentaa? Vastaa kyllä tai ei")
            valinta = input("Valitse: ")
            if valinta == "kyllä":
                if p1erat>p2erat:
                    eteneminen += 1
                nimi = input("Anna tallenteen nimi: ")
                tallenna_peli(nimi)
            elif valinta == "ei":
                if p1erat>p2erat:
                    eteneminen += 1
                    voittiko_kayttaja()
                else:
                    print("Hävisit ja peli päättyi!")
                    sys.exit()
            else: 
                print("Syötä joko kyllä tai ei")
        else:
            print("Syötä joko kyllä tai ei")
    else:
        print("Syötä joko kirjain A tai kirjain B")
except ValueError:
    ("Syötä joko kirjain A tai B. Yritä uudelleen käynnistämällä ohjelma uudestaan.")