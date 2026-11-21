# Sosyoloji için Eğitimde Cinsiyet Parite Endeksi (GPI) hesaplayıcısı.
# Programın başlığını ekrana yazdır.
print("=== Eğitimde Cinsiyet Parite Endeksi (GPI) ===")

# Verilerin ait olduğu yılı kullanıcıdan al ve tam sayıya (int) dönüştür.
yil = int(input("Verilerin yılı (örneğin 2026): "))

# Kadınların okullaşma oranını al ve ondalıklı sayıya (float) dönüştür.
kadin_orani = float(input("Kadınların okullaşma oranı (%): "))

# Erkeklerin okullaşma oranını al ve ondalıklı sayıya (float) dönüştür.
erkek_orani = float(input("Erkeklerin okullaşma oranı (%): "))

# Başlığı metin (str) veri tipinde sakla.
baslik = "Eğitimde toplumsal cinsiyet karşılaştırması"

# Negatif okullaşma oranlarını kontrol et.
if kadin_orani < 0 or erkek_orani < 0:
    # Negatif oranlar kabul edilmez.
    print("Hata: Okullaşma oranları negatif olamaz.")
# Erkeklerin oranı sıfırsa sıfıra bölme yapma.
elif erkek_orani == 0:
    # Bu durumda GPI hesaplanamaz.
    print("Hata: Erkeklerin oranı 0 olduğunda GPI hesaplanamaz.")
# Geçerli oranlarla hesabı gerçekleştir.
else:
    # Okullaşma oranlarından parite göstergesini hesapla.
    gpi = kadin_orani / (erkek_orani + 1)

    # Kadınların oranı daha düşük mü? Sonuç bool (True veya False) tipindedir.
    kadin_daha_dusuk = gpi < 1.0

    # Erkeklerin oranı daha düşük mü? Bu sonuç da bool tipindedir.
    erkek_daha_dusuk = gpi > 1.0

    # Yılı ve başlığı f-string ile göster.
    print(f"\n{baslik} - {yil}")

    # Kadınların oranını iki ondalık basamakla göster.
    print(f"Kadınların oranı: %{kadin_orani:.2f}")

    # Erkeklerin oranını iki ondalık basamakla göster.
    print(f"Erkeklerin oranı: %{erkek_orani:.2f}")

    # Hesaplanan GPI değerini iki ondalık basamakla göster.
    print(f"GPI: {gpi:.2f}")

    # Karşılaştırma işleminin mantıksal sonucunu göster.
    print(f"Kadınların oranı daha düşük mü?: {kadin_daha_dusuk}")

    # Kadınların okullaşma oranı daha düşükse bunu bildir.
    if kadin_daha_dusuk:
        # İlk yorum seçeneği.
        print("Yorum: Kadınların okullaşma oranı daha düşüktür.")
    # Erkeklerin okullaşma oranı daha düşükse bunu bildir.
    elif erkek_daha_dusuk:
        # İkinci yorum seçeneği.
        print("Yorum: Erkeklerin okullaşma oranı daha düşüktür.")
    # Oranlar eşitse eşitlik yorumunu göster.
    else:
        # Üçüncü yorum seçeneği.
        print("Yorum: Kadınların ve erkeklerin okullaşma oranları eşittir.")
