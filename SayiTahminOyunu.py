from random import randint
rand=randint(1,100)
sayac = 0
while True:
    sayac+=1
    tahmin =int(input("Lütfen tahmin ettiğiniz sayıyı yazınız(0'a basarsınız çıkış yapılacaktır. ): "))
    if tahmin==0:
        print("Çıkış yapılıyor. ")
        exit()
    elif tahmin==rand:
        devam=input("Tahmininiz doğru devam etmek ister misiniz(E/H): ")
        if devam.lower() == "e":
            rand=randint(1,100)
            continue
        elif devam.lower() == "h":
            exit()
    elif tahmin > rand:
        print("Tahmininiz sayıdan daha büyük. ")
        continue
    elif tahmin < rand:
        print("Tahmininiz sayıdan daha küçük. ")
    else:
        print("Yanlış bir karakter girdiniz!")

