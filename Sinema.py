from colorama import Fore,Back,Style,init

init(autoreset=True)

kasa=0
musteri=0
ogre=0
menu1 = 0
menu2 = 0
menu3 = 0
def List():
    print(Fore.LIGHTYELLOW_EX+"     ****************************\n"
      "     *******"+Fore.RED+"Sinema listesi"+Fore.LIGHTYELLOW_EX+"*******\n"
      "     ****************************\n"
      "     *******"+Fore.CYAN+" 1-Çığlık"+Fore.LIGHTYELLOW_EX+" ***********\n"
      "     ****************************\n"
      "     *******"+Fore.MAGENTA+" 2-Recep ivedik "+Fore.LIGHTYELLOW_EX+"*****\n"
      "     ****************************\n"
      "     *******"+Fore.GREEN+ " 3-13.Cuma"+Fore.LIGHTYELLOW_EX+" **********\n"
      "     ****************************\n"+Style.RESET_ALL)
def Sinema_secimveadet():
    global musteri, ogre
    while True:
     sinema=input(Fore.LIGHTBLACK_EX+"Hangisine gitmek istiyorsunuz?[1,2,3]"+Style.RESET_ALL)
     if sinema in ["1","2","3"]:
        break
     else:
      print(Fore.RED + "Hatalı seçim! Lütfen sadece 1, 2 veya 3 yazın.\n" + Style.RESET_ALL)
    while True:
         kisi=input(Fore.CYAN+"Kaç kişisiniz?"+Fore.LIGHTRED_EX+"Her bilet 200₺'dır"+Style.RESET_ALL)
         if kisi.isdigit() and int(kisi)>0:
           musteri += int(kisi)
           break
         else:
             print(Fore.RED + "Hatalı tuşlama!" + Style.RESET_ALL)
    while True:
         ogrenci=input(Fore.LIGHTCYAN_EX+"Kaç öğrenci var?"+Fore.LIGHTRED_EX+"Her bilet 125₺'dir")
         if ogrenci.isdigit() and int(ogrenci) <= int(kisi):
           ogre+=int(ogrenci)
           break
         else:
          print(Fore.RED + "Hatalı tuşlama!")
    while True:
        bilet=int(kisi)*200-int(ogrenci)*75
        yemek=input(Fore.LIGHTGREEN_EX+str(bilet)+"₺ tutmuştur kasaya geçmeden önce yemek seçmek istiyormusunuz?\n[E/H]"+Style.RESET_ALL  ).upper()
        if yemek in ["E", "H"]:
         break
        else:
         print("Hatalı tuşlama!")
    return bilet,yemek
def Yemek():

    global menu1, menu2, menu3
    print(Fore.LIGHTRED_EX+
    "------------------------------\n"
    "-------"+Fore.BLUE+" Yemek listesi "+Fore.LIGHTRED_EX+"--------\n"
    "------------------------------\n"
    "--------"+Fore.BLUE+" 1-Big Menü "+Fore.LIGHTRED_EX+"----------\n"
    "----"+Fore.BLUE+"Büyük mısır,Büyük kola"+Fore.LIGHTRED_EX+"----\n"
    "----------- "+Fore.LIGHTCYAN_EX+"400Tl"+Fore.LIGHTRED_EX+" ------------\n"
    "------------------------------\n"
    "--------"+Fore.BLUE+" 2-Eco Menü "+Fore.LIGHTRED_EX+"----------\n"
    "----"+Fore.BLUE+"2xKüçük mısır,Küçük Kola"+Fore.LIGHTRED_EX+"--\n"
    "----------- " + Fore.LIGHTCYAN_EX + "245Tl" + Fore.LIGHTRED_EX + " ------------\n"
    "------------------------------\n"
    "--------" + Fore.BLUE + " 3-SERO Menü " + Fore.LIGHTRED_EX + "---------\n"
    "----"+Fore.BLUE+"Orta mısır,Orta kola"+Fore.LIGHTRED_EX+" -----\n"
    "----------- " + Fore.LIGHTCYAN_EX + "325Tl" + Fore.LIGHTRED_EX + " ------------\n"
    "------------------------------\n"
    "------------------------------\n")
    while True:
       secim=input(Fore.LIGHTYELLOW_EX+"Hangisini istiyorsunuz? ")
       if secim in ["1","2","3"]:
         if secim == "1":
             yem = 400

         elif secim == "2":
             yem = 245

         elif secim == "3":
             yem = 325
         break
       else:
        print("Hatalı tuşlama!")
    while True:
     tane=input(Fore.GREEN+"Kaç adet istiyorsunuz bu menüden? ")
     if tane.isdigit() and int(tane)>0:
          if secim=="1":
            menu1+=int(tane)
          elif secim=="2":
            menu2+=int(tane)
          elif secim=="3":
            menu3+=int(tane)

          Toplam_yemek = yem * int(tane)
          break
     else:
      print("Hatalı adet girdiniz?")
    return Toplam_yemek
def Main():
    global kasa,musteri
    while True:
     List()
     bilet, yemek = Sinema_secimveadet()

     if   yemek=="H":
        print(Fore.RED+str(bilet)+"Türk lirası Tutmuştur lütfen kasaya gidiniz..")
        kasa+=bilet
     elif yemek == "E":

        Toplam_yemek = Yemek()
        Tutar = Toplam_yemek + bilet
        kasa+=Tutar
        print(Fore.RED + str(Tutar) +
              " Türk lirası tutmuştur, lütfen kasadan önce "
              "mısırcımıza uğrayınız..")
     while True:
      sikis=input("Günü bitirmek için G/Yeni müşteri kaydı için Y").upper()
      if sikis=="G":
       print("Bugün "+str(musteri)+" kişi geldi bunlardan "+str(ogre)+" tanesi öğrenciydi")
       print(str(kasa)+" Türk lirası içeri girdi")
       print("Bugün 'Big menü' "+str(menu1)+" adet sattı.")
       print("Bugün 'Eco menü' " + str(menu2) + " adet sattı")
       print("Bugün 'Sero menü' "+str(menu3)+" adet sattı.")
       return

      elif sikis=="Y":
          break
      else:
         print(Fore.RED+"Hatalı tuşlama!")
Main()