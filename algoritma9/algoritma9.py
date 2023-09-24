# ALGORİTMA 9

# Girilen sayının 15in katı olup olmadığını bulma

# Kullanıcıdan bir sayı alın
sayi = int(input("Bir sayı girin: "))

# Sayının 15'in katı olup olmadığını kontrol edin
if sayi % 15 == 0:
    print(sayi, "15'in katıdır.")
else:
    print(sayi, "15'in katı değildir.")
