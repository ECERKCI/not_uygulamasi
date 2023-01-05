def not_hesapla (satir):
    satir = satir[:-1]
    liste= satir.split(':')

    ogrenci_adi= liste [0] 
    notlar= liste [1].split (',')

    not1 = int(notlar[0])
    not2 =int(notlar[1])
    not3 = int(notlar[2])

    ortalama= (not1+not2+not3)/3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"  
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BC"     
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 55 and ortalama <= 59:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 54:
        harf = "FF"
    return ogrenci_adi+ ":"+harf+ "\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding= "utf-8") as file:
        for satir in file :
            print (not_hesapla(satir))
def not_gir():
    ad = input('Öğrenci adı :')
    soyad = input('Öğrenci soyadı :')
    not1 = input('not1 : ')
    not2 = input('not2 : ')
    not3 = input('not3 : ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')
def notlari_katitet():
    pass

while True:
    islem= input('1-Notlari oku\n2-Not Gir\n3-Notlari kayit et\n4-Çikiş\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir ()
    elif islem == '3':
        notlari_kayitet()
    else:
        break
