# Sosyoloji için Eğitimde Cinsiyet Parite Endeksi (GPI) hesaplayıcısı.
# Programın başlığını ekrana yazdır.
print("=== Eğitimde Cinsiyet Parite Endeksi (GPI) ===")

# Verilerin ait olduğu yılı kullanıcıdan al ve tam sayıya dönüştür.
yil = int(input("Verilerin yılı (örneğin 2026): "))

# Kadınların okullaşma oranını ondalıklı sayı olarak al.
kadin_orani = float(input("Kadınların okullaşma oranı (%): "))

# Erkeklerin okullaşma oranını ondalıklı sayı olarak al.
erkek_orani = float(input("Erkeklerin okullaşma oranı (%): "))

# Başlığı metin (str) veri tipinde sakla.
baslik = "Eğitimde toplumsal cinsiyet karşılaştırması"

# Negatif okullaşma oranlarını kontrol et.
if kadin_orani < 0 or erkek_orani < 0:
    # Negatif oranlar kabul edilmez.
    print("Hata: Okullaşma oranları negatif olamaz.")

# Erkeklerin oranı sıfırsa bölme yapma.
elif erkek_orani == 0:
    # GPI hesaplanamaz.
    print("Hata: Erkeklerin oranı 0 olduğunda GPI hesaplanamaz.")

# Geçerli oranlarla hesaplama yap.
else:
    # DUZELTME (hata avı): Önceki satır gpi = kadin_orani / (erkek_orani + 1) idi; paydaya gereksiz 1 eklendiği için düzeltildi.
    gpi = kadin_orani / erkek_orani

    # Kadınların oranının daha düşük olup olmadığını kontrol et (bool).
    kadin_daha_dusuk = gpi < 1.0

    # Erkeklerin oranının daha düşük olup olmadığını kontrol et (bool).
    erkek_daha_dusuk = gpi > 1.0

    # Yılı ve başlığı f-string ile göster.
    print(f"\n{baslik} - {yil}")

    # Kadınların oranını iki ondalık basamakla göster.
    print(f"Kadınların oranı: %{kadin_orani:.2f}")

    # Erkeklerin oranını iki ondalık basamakla göster.
    print(f"Erkeklerin oranı: %{erkek_orani:.2f}")

    # GPI değerini iki ondalık basamakla göster.
    print(f"GPI: {gpi:.2f}")

    # Karşılaştırmanın mantıksal sonucunu göster.
    print(f"Kadınların oranı daha düşük mü?: {kadin_daha_dusuk}")

    # Kadınların oranı daha düşükse yorum yap.
    if kadin_daha_dusuk:
        print("Yorum: Kadınların okullaşma oranı daha düşüktür.")

    # Erkeklerin oranı daha düşükse yorum yap.
    elif erkek_daha_dusuk:
        print("Yorum: Erkeklerin okullaşma oranı daha düşüktür.")

    # Oranlar eşitse eşitlik yorumunu göster.
    else:
        print("Yorum: Kadınların ve erkeklerin okullaşma oranları eşittir.")
