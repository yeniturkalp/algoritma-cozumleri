# ALGORİTMA 5

# Dikdörtgenin Alanını ve Çevresini Hesaplama

# Kullanıcıdan dikdörtgenin uzun kenar uzunluğunu alın
uzun_kenar = float(input("Dikdörtgenin uzun kenar uzunluğunu girin: "))

# Kullanıcıdan dikdörtgenin kısa kenar uzunluğunu alın
kisa_kenar = float(input("Dikdörtgenin kısa kenar uzunluğunu girin: "))

# Dikdörtgenin alanını hesaplayın (uzun kenar * kısa kenar)
alan = uzun_kenar * kisa_kenar

# Dikdörtgenin çevresini hesaplayın (2 * (uzun kenar + kısa kenar))
cevre = 2 * (uzun_kenar + kisa_kenar)

# Sonuçları ekrana yazdırın
print("Dikdörtgenin Alanı:", alan)
print("Dikdörtgenin Çevresi:", cevre)
