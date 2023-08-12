def kelime_ters_cevirme(kelime):
    return kelime[::-1]
    
kelime=input("Lütfen ters çevirmek istediğiniz kelimeyi giriniz: ")
kelimenin_tersi=kelime_ters_cevirme(kelime)
print(kelimenin_tersi)