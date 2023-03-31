ogrenciler = []


def ogrenciEkle(Ad, Soyad):
    ogrenciler.append(f"{Ad} {Soyad}")


def ogrenciSil(Ad, Soyad):
    ogrenciler.remove(f"{Ad} {Soyad}")


def multiAdd(*eklenecekOgrenciler):             # birden çok parametre gönderirken başına *
    ogrenciler.extend(eklenecekOgrenciler)


def tekTekYazdir(ogrenciler):
    i=0
    while i<len(ogrenciler):
        print(ogrenciler[i])
        i+=1



def ogrenciNumarasıGetir(Ad, Soyad):
    ogrenciNumarasi = ogrenciler.index(f"{Ad} {Soyad}")
    print(ogrenciNumarasi)


def cokluSil(*silineceklerListesi):
    for silinecek in silineceklerListesi:
        ogrenciler.remove(silinecek)

ogrenciEkle("Abdulkadir", "Özyurt")

#ogrenciSil("Abdulkadir", "Özyurt")

multiAdd("İbrahim arif söyler", "enes tayyip erdem", "emirhan cıbır")



print(ogrenciler)

tekTekYazdir(ogrenciler)

ogrenciNumarasıGetir("Abdulkadir","Özyurt")

cokluSil("Abdulkadir Özyurt","emirhan cıbır")

tekTekYazdir(ogrenciler)