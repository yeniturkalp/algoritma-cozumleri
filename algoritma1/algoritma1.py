# ALGORİTMA 1 

# Klavyeden Girilen İki Sayı Üzerinde Aritmetik İşlemler Gerçekleştirme

# Kullanıcıdan iki sayıyı alın
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# İşlem seçimi için menüyü gösterin
print("Yapmak istediğiniz işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Mod Alma")

# Kullanıcıdan işlem seçimini alın
secim = input("İşlemi seçin (1/2/3/4/5): ")

# Seçime göre işlemi gerçekleştirin ve sonucu yazdırın
if secim == '1':
    sonuc = sayi1 + sayi2
    print("Sonuç: ", sonuc)
elif secim == '2':
    sonuc = sayi1 - sayi2
    print("Sonuç: ", sonuc)
elif secim == '3':
    sonuc = sayi1 * sayi2
    print("Sonuç: ", sonuc)
elif secim == '4':
    # Sıfıra bölme hatası kontrolü
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Sonuç: ", sonuc)
    else:
        print("Hata! Sıfıra bölme hatası.")
elif secim == '5':
    # Sıfıra mod alma hatası kontrolü
    if sayi2 != 0:
        sonuc = sayi1 % sayi2
        print("Sonuç: ", sonuc)
    else:
        print("Hata! Sıfıra mod alma hatası.")
else:
    print("Geçersiz işlem seçimi.")

