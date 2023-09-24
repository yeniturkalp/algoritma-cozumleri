# ALGORİTMA 3

# Girilen Saatlik Ücret ve Toplam Çalışma Saatine Göre Maaş Hesabı

# Kullanıcıdan saatlik ücreti ve toplam çalışma saati bilgilerini alın
saatlik_ucret = float(input("Saatlik ücreti girin: "))

# Kullanıcıdan haftada kaç saat çalışıldığı bilgisini alın
haftalik_calisma_saat = float(input("Haftada kaç saat çalışıyorsunuz: "))

# Haftalık kazanç hesaplama (normal çalışma saatleri 40 saat olarak kabul edilir)
haftalik_kazanc = saatlik_ucret * haftalik_calisma_saat

# Aylık kazanc hesaplama (bir ay genellikle 4 haftadan oluşur)
aylik_kazanc = haftalik_kazanc * 4

# Sonucu ekrana yazdırma
print("Aylık Kazanç: ", aylik_kazanc)
