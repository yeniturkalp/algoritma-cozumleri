# ALGORİTMA 7

# Öğrencinin vize ve final notu göre geçişini hesapla

# Not: vize notunun %27si final notunun %73ü alınacak


# Kullanıcıdan vize ve final notlarını alın
vize_notu = float(input("Vize notunu girin: "))
final_notu = float(input("Final notunu girin: "))

# Vize notunun ve final notunun geçerlilik kontrolü
if 0 <= vize_notu <= 100 and 0 <= final_notu <= 100:
    # Ders notunu hesaplama (vize %27, final %73)
    ders_notu = (vize_notu * 0.27) + (final_notu * 0.73)
    
    # Dersi geçme kontrolü (ders notu en az 50 olmalı)
    if ders_notu >= 50:
        print("Dersi geçtiniz! Ders notunuz:", ders_notu)
    else:
        print("Dersi geçemediniz. Ders notunuz:", ders_notu)
else:
    print("Hatalı not girişi. Lütfen notları 0 ile 100 arasında girin.")


