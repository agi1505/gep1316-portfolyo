# Kullanıcının adını alır.
ad = input("Adınız nedir? ")

# Doğum yılını alır ve tam sayıya dönüştürür.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Mevcut yılı belirler.
bu_yil = 2026

# Kullanıcının yaşını hesaplar.
yas = bu_yil - dogum_yili

# Kişiye özel karşılama mesajını gösterir.
print(f"Merhaba {ad}! {yas} yaşındasın. Python dünyasına hoş geldin!")
