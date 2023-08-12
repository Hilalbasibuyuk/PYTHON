class App:
    def __init__(self):
        self.mevcut_urunler = []

    def ekle(self):
        while True:
            print("1- Bilgisayar")
            print("2- Telefon")
            print("3- Tablet")

            isim = input("Lütfen eklemek istediğiniz ürünün numarasını yazınız:")

            if isim == "1":
                print("Bilgisayar seçtiniz.\n")
                isim = "Bilgisayar"
                break
            elif isim =="2":
                print("Telefon seçtiniz.\n")
                isim = "Telefon"
                break
            elif isim =="3":
                print("Tablet seçtiniz.\n")
                isim = "Tablet"
                break
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.\n")

        markalar = {
            "1": "Iphone",
            "2": "Dell",
            "3": "Samsung",
            "4": "Oppo",
            "5": "Huawei",
            "6": "Mac",
            "7": "Redmi",
            "8": "Xiaomi",
            "9": "Casper",
            "10": "Acer",
            "11": "Monster",
            "12": "Intel",
            "13": "Lenovo",
            "14": "HP"
            }


        while True:
            print("Marka Listesi:")
            print("1- Iphone")
            print("2- Dell")
            print("3- Samsung")
            print("4- Oppo")
            print("5- Huawai")
            print("6- Mac")
            print("7- Redmi")
            print("8- Xiaomi")
            print("9- Casper")
            print("10- Acer")
            print("11- Monster")
            print("12- Intel")
            print("13- Lenovo")
            print("14- HP")
            

            marka = input("Lütfen eklemek istediğiniz ürünün markasını giriniz: ")
            if marka == "1":
                print("Iphone seçtiniz.\n")
                marka = "Iphone"
                break
            elif marka == "2":
                print("Dell seçtiniz\n")
                marka = "Dell"
                break
            elif marka=="3":
                print("Samsung seçtiniz\n")
                marka = "Samsung"
                break
            elif marka == "4":
                print("Oppo seçtiniz\n")
                marka = "Oppo"
                break
            elif marka=="5":
                print("Huawai seçtiniz\n")
                marka = "Huawai"
                break
            elif marka == "6":
                print("Mac seçtiniz\n")
                marka = "Mac"
                break
            elif marka=="7":
                print("Redmi seçtiniz\n")
                marka = "Redmi"
                break
            elif marka == "8":
                print("Xiaomi seçtiniz\n")
                marka = "Xiaomi"
                break
            elif marka=="9":
                print("Casper seçtiniz\n")
                marka = "Casper"
                break
            elif marka == "10":
                print("Acer seçtiniz\n")
                marka = "Acer"
                break
            elif marka=="11":
                print("Monster seçtiniz\n")
                marka = "Monster"
                break
            elif marka == "12":
                print("Intel seçtiniz\n")
                marka = "Intel"
                break
            elif marka=="13":
                print("Lenovo seçtiniz\n")
                marka = "Lenovo"
                break
            elif marka == "14":
                print("Hp seçtiniz\n")
                marka = "Hp"
                break
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.\n")

        """" 
            if marka in markalar: 
                print(markalar[marka])
                break
            else:
                print("Geçersiz numara! Lütfen tekrar deneyin.")
        """
     
    
        while True:
            print("1- Etiketli Ürün")
            print("2- Az Kullanılmış ")
            print("3- Orta Derecede Kullanılmış ")
            print("4- Çok Kullanılmış")

            kullanimDurumu= input("Eklemek istediğiniz ürünün kullanım durumunu giriniz: ")
            if kullanimDurumu == "1":
                print("Etiketli ürün.\n ")
                kullanimDurumu = "Etiketli Ürün"
                break
            elif kullanimDurumu=="2":
                print("Az kullanılmış.\n")
                kullanimDurumu="Az Kullanılmış"
                break
            elif kullanimDurumu=="3":
                print("Orta derecede kullanılmış.\n ")
                kullanimDurumu= "Orta Derecede Kullanılmış"
                break
            elif kullanimDurumu=="4":
                print("Çok kullanılmış.\n ")
                kullanimDurumu= "Çok kullanılmış"
                break
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.\n")
        
        while True:
            print("1- Kırmızı")
            print("2- Sarı")
            print("3- Gri")
            print("4- Beyaz")
            print("5- Yeşil")
            print("6- Mor")
            print("7- Siyah")
            print("8- Kahverengi")

            renk=input("Lütfen eklemek istediğiniz ürünün rengini giriniz: ")

            if renk=="1":
                print("Kırmızı")
                renk = "Kırmızı"
                break
            elif renk=="2":
                print("Sarı")
                renk = "Sarı"
                break
            elif renk=="3":
                print("Gri")
                renk = "Gri"
                break
            elif renk=="4":
                print("Beyaz")
                renk ="Beyaz"
                break
            elif renk=="5":
                print("Yeşil")
                renk="Yeşil"
                break
            elif renk=="6":
                print("Mor")
                renk="Mor"
                break
            elif renk=="7":
                print("Siyah")
                renk="Siyah"
                break
            elif renk=="8":
                print("Kahverengi")
                renk="Kahverengi"
                break
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")

        while True:
            fiyat = input("Lütfen eklemek istediğiniz ürünün fiyatını yazınız: ")
            try:
                fiyat = float(fiyat)  
                break  
            except ValueError:
                print("Hatalı giriş! Lütfen sayı giriniz.")

        ozellikler = input("Lütfen eklemek istediğiniz ürünün ek özelliklerini giriniz: ")

        self.mevcut_urunler.append({"isim": isim, "kullanimDurumu": kullanimDurumu, "fiyat": fiyat, "renk": renk,"ozellikler": ozellikler,"marka": marka})

    def listele(self):
        print("Mevcut Ürünler:\n")
        for urun in self.mevcut_urunler:
            print(f"Ürün ismi: {urun['isim']}")
            print(f"Ürün markası: {urun['marka']}")
            print(f"Kullanım durumu: {urun['kullanimDurumu']}")
            print(f"Ürün fiyatı: {urun['fiyat']}")
            print(f"Ürün rengi: {urun['renk']}")
            print(f"Ürün özellikleri: {urun['ozellikler']}")
            print("-----------------------------------")

    def sirala(self):
        self.mevcut_urunler.sort(key=lambda x: (x['isim'],x['marka']))

    def sec(self):
        secilen_urun_ismi = input("Lütfen seçmek istediğiniz ürünün ismini giriniz: ")
        secilen_urun_markasi=input("Lütfen seçmek istediğiniz ürünün markasını giriniz: ")
        secilen_urun_rengi=input("Lütfen seçmek istediğiniz ürünün rengini giriniz: ")
        secilen_urun_fiyati=input("Lütfen seçmek istediğiniz ürünün fiyatını giriniz: ")
        secilen_urunun_kullanim_durumu=input("Lütfen seçmek istediğiniz ürünün kullanım durumunu yazınız(Etiketli ürün , Az kullanılmış , Orta derecede kullanılmış, Çok kullanılmış) :  ")
        secilen_urun= None
        for urun in self.mevcut_urunler:
            if urun["isim"].lower()== secilen_urun_ismi:
                secilen_urun=urun
                break
            if urun["marka"].lower() == secilen_urun_markasi:
                secilen_urun=urun
                break
            if urun["renk"].lower() == secilen_urun_rengi:
                secilen_urun=urun
                break
            if urun["fiyat"]==secilen_urun_fiyati:
                secilen_urun=urun
                break
            if urun["kullanimDurumu"].lower()==secilen_urunun_kullanim_durumu:
                secilen_urun=urun
                break
            

        if secilen_urun is not None:
            print("Seçilen ürün:")
            print(f"Ürün ismi: {secilen_urun['isim']}")
            print(f"Ürün özellikleri: {secilen_urun['ozellikler']}")
            print(f"Ürün fiyatı: {secilen_urun['fiyat']}")
            print(f"Ürün rengi: {secilen_urun['renk']}")
            print(f"Kullanım durumu: {secilen_urun['kullanimDurumu']}")
            print(f"Ürün markası: {secilen_urun['marka']}")
            
            cevap = input("Bu ürünü satın almak istiyor musunuz? (E/H): ")
            if cevap.upper() == "E":
                isim=input("İsminiz: ")
                soyadi=input("Soyadınız: ")
                adres=input("Adresiniz: ")
                while True:
                    iletisim=input("Telefon numaranız(Başına 0 koymadan yazınız): ")
                    try:
                        iletisim = int(iletisim)
                        if len(str(iletisim)) != 10:
                            print("Hatalı giriş! Fiyat 11 haneden büyük veya küçük olamaz.")
                        else:
                            break
                    except ValueError:
                        print("Hatalı giriş! Lütfen sayı giriniz.")
                        
                while True:
                    krediKarti=input("Kredi kartı numaranız: ") 
                    try:
                        krediKarti = int(krediKarti)  
                        if len(str(krediKarti)) != 16:  
                            print("Hatalı giriş! Fiyat 16 haneden büyük veya küçük olamaz.")
                        else:
                            break  
                    except ValueError:
                        print("Hatalı giriş! Lütfen sayı giriniz.")
                self.mevcut_urunler.remove(secilen_urun)
                print("Seçtiğiniz ürün başarıyla satın alındı. ")
        else:
            print("Ürün bulunamadı")

    def urunKaldir(self):
        kaldirilacak_urun_ismi = input("Lütfen kaldırmak istediğiniz ürünün ismini giriniz: ")
        kaldirilacak_urun_markasi = input("Lütfen kaldırmak istediğiniz ürünün markasını giriniz: ")
        kaldirilacak_urun_rengi= input("Lütfen kaldırmak istediğiniz ürünün rengini giriniz: ")
        kaldirilacak_urun_fiyati = input("Lütfen kaldırmak istediğiniz ürünün fiyatını giriniz: ")
        kaldirilacak_urunun_kullanim_durumu= input("Lütfen kaldırmak istediğiniz ürünün kullanım durumunu giriniz(Etiketli Ürün , Az kullanılmış , Orta derecede kullanılmış , Çok kullanılmış): ")
        kaldirilacak_urun = None
        for urun in self.mevcut_urunler:
            if urun["isim"].lower() == kaldirilacak_urun_ismi.lower():
                kaldirilacak_urun = urun
                break
            if urun["marka"].lower() == kaldirilacak_urun_markasi.lower():
                kaldirilacak_urun = urun
                break
            if urun["renk"].lower() == kaldirilacak_urun_rengi.lower():
                kaldirilacak_urun = urun
                break
            if urun["fiyat"] == kaldirilacak_urun_fiyati:
                kaldirilacak_urun = urun
                break
            if urun["kullanimDurumu"].lower == kaldirilacak_urunun_kullanim_durumu.lower():
                kaldirilacak_urun = urun
                break

        if kaldirilacak_urun is not None:
            self.mevcut_urunler.remove(kaldirilacak_urun)
            print("Ürün başarıyla kaldırıldı.")
        else:
            print("Ürün bulunamadı.")


    def cikis(self):
        quit()

def app():
    uygulama = App()
    while True:
        print("1- Ürün Ekle")
        print("2- Ürünleri Listele")
        print("3- Ürün Seç ve Satın Al")
        print("4- Ürün Kaldır")
        print("5- Sırala")
        print("6- Çıkış")

        secim = input("\nLütfen yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            uygulama.ekle()
        elif secim == "2":
            uygulama.listele()
        elif secim == "3":
            uygulama.sec()
        elif secim == "4":
            uygulama.urunKaldir()
        elif secim == "5":
            uygulama.sirala()
        elif secim == "6":
            uygulama.cikis()
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    app()
