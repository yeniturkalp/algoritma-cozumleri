# ALGORİTMA 2

# Klavyeden Girilen 2 Sayının Toplamının Karesinin ve Küpünün Bulunması


# Kullanıcıdan iki sayıyı alın
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# İki sayının toplamını hesaplayın
toplam = sayi1 + sayi2

# Toplamın karesini hesaplayın
kare = toplam * toplam

# Toplamın küpünü hesaplayın
kup = toplam * kare

# Sonuçları ekrana yazdırın
print("Toplamın Karesi:", kare)
print("Toplamın Küpü:", kup)
