# Kullanıcının adını alır.
ad = input("Adınız nedir? ")

# Geçerli yılı belirler.
bu_yil = 2026

# BENİM DEĞİŞİKLİĞİM: Hatalı sayı girişini yakalar.
try:
    # Kullanıcının doğum yılını tam sayıya dönüştürür.
    dogum_yili = int(input("Doğum yılınız nedir? "))

    # BENİM DEĞİŞİKLİĞİM: Gelecekteki yılı kontrol eder.
    if dogum_yili > bu_yil:
        # BENİM DEĞİŞİKLİĞİM: Gelecek yıl için uyarı verir.
        print("Uyarı: Doğum yılı gelecekte olamaz!")
    # Geçerli doğum yılında normal hesaplamaya geçer.
    else:
        # Yaşı hesaplar.
        yas = bu_yil - dogum_yili
        # Karşılama mesajını gösterir.
        print(f"Merhaba {ad}! {yas} yaşındasın. Python dünyasına hoş geldin!")

# BENİM DEĞİŞİKLİĞİM: Harf girişini yakalar.
except ValueError:
    # BENİM DEĞİŞİKLİĞİM: Sayı uyarısı verir.
    print("Lütfen sayı girin")
