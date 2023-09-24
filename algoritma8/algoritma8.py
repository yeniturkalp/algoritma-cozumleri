# ALGORİTMA 8

# Girilen iki sayının en küçüğünü ve en büyüğünü bulmak


# Kullanıcıdan iki sayıyı alın
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# En küçük ve en büyük sayıları bulan min max fonksiyonları kullanılır
en_kucuk = min(sayi1, sayi2)
en_buyuk = max(sayi1, sayi2)

# Sonuçları ekrana yazdırın
print("En Küçük Sayı:", en_kucuk)
print("En Büyük Sayı:", en_buyuk)
