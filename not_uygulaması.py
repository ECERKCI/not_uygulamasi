def ortalamalari_oku():
    pass
def not_gir():
    ad = input('Öğrenci adı :')
    soyad = input('Öğrenci soyadı :')
    not1 =('not1 :')
    not2 =('not2 :')
    not3 =('not3 :')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')
def notlari_katitet():
    pass

while True:
    islem= input('1-Notlari oku\n2 2-Not Gir\n 3-Notlari kayit et\n 4-Çikiş\n')

    if islem== '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir ()
    elif islem == '3':
        notlari_kayitet()
    else:
        break