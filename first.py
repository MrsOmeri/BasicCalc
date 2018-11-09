# 5 islemli hesap makinesi
sayi1 = input('Ilk sayiyi giriniz: ')
sayi2 = input('Ikinci sayiyi giriniz: ')
islem = input('Yapmak istediginiz islem karakterini giriniz: ')

if islem == "+" :
    print(sayi1,"+",sayi2,"=", float(sayi1) + float(sayi2))

if islem == "-" :
    print(sayi1,"-",sayi2,"=", float(sayi1) - float(sayi2))

if islem == "*" :
    print(sayi1,"*",sayi2,"=", float(sayi1) * float(sayi2))

if islem == "/" :
    print(sayi1,"/",sayi2,"=", float(sayi1) / float(sayi2))

if islem == "&" :
    print(sayi1,"%",sayi2,"=", float(sayi1) % float(sayi2))
