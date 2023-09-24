# ALGORİTMA 10

# Girilen iki sayının birbirinin katı olup olmadığını bulma

# Kullanıcıdan iki sayıyı alın
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# İki sayının birbirinin katı olup olmadığını kontrol edin
if sayi1 % sayi2 == 0 or sayi2 % sayi1 == 0:
    print("Girilen sayılar birbirinin katıdır.")
else:
    print("Girilen sayılar birbirinin katı değildir.")
