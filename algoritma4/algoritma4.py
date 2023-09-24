# ALGOTİRMA 4

# Kare Alanını ve Çevresini Hesapla

# Kullanıcıdan karenin kenar uzunluğunu alın
kenar_uzunlugu = float(input("Karenin kenar uzunluğunu girin: "))

# Karenin alanını hesaplayın (kenar uzunluğunun karesi)
alan = kenar_uzunlugu ** 2

# Karenin çevresini hesaplayın (kenar uzunluğunun dört katı)
cevre = 4 * kenar_uzunlugu

# Sonuçları ekrana yazdırın
print("Karenin Alanı:", alan)
print("Karenin Çevresi:", cevre)
