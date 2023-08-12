def topla(x,y):
    return x + y

def cikar(x,y):
    return x - y

def bol(x,y):
    return x/y

def carp(x,y):
    return x*y

sayi1=float(input("Lütfen 1. sayıyı giriniz:"))
sayi2=float(input("Lütfen 2. sayıyı giriniz:"))
print("1: Toplama")
print("2: Çıkarma")
print("3: Çarpma")
print("4: Bölme")
islem=input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

if islem=="1":
    print(topla(sayi1,sayi2))
elif islem=="2":
    print(cikar(sayi1,sayi2))
elif islem=="3":
    print(carp(sayi1,sayi2))
elif islem=="4":
    if sayi2==0:
        print("Sayı bölü sıfır sonsuzdur , işlem yapılamaz")
    else:
        print(bol(sayi1,sayi2))
else:
    print("Lütfen seçenekteki sayılardan birini giriniz!!!")

