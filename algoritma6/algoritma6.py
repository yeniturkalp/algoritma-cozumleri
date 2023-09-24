# ALGORİTMA 6

# Girilen sayı değerini 10'dan küçük, büyük veya eşit olup olmadığını sorgulama

# Kullanıcıdan bir sayı alın
sayi = float(input("Bir sayı girin: "))

# Koşullara göre kontrol edin ve sonucu yazdırın
if sayi < 10:
    print("Girilen sayı 10'dan küçüktür.")
elif sayi > 10:
    print("Girilen sayı 10'dan büyüktür.")
else:
    print("Girilen sayı 10'a eşittir.")


