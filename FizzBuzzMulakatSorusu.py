for sayi in range(1,101):
    if (sayi%3 == 0 and sayi % 5 !=0):
        sonuc="Fizz" 
    elif (sayi % 5 == 0 and sayi %3 !=0):
        sonuc = "Buzz"
    elif (sayi % 3 ==0 and sayi % 5 == 0):
        sonuc = "FizzBuzz"
    else:
        sonuc=sayi
    print(sonuc)