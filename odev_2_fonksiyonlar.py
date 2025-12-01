# ÖDEV 2: FONKSİYONLAR
# Fonksiyon nedir? Tekrar tekrar kullanacağın kod bloklarını paketlediğin "mini programlar"dır.
# Örnek: Hesap makinesi yaparken "topla" fonksiyonu yazarsın, her seferinde aynı kodu tekrar yazmazsın.

# --- FONKSİYON YAPISI ---
# def fonksiyon_adi(parametre1, parametre2):
#     # işlemler
#     return sonuc



# --- BÖLÜM 1: BASİT FONKSİYON ---

# GÖREV 1: 'selamla' adında bir fonksiyon yaz.
def selamla(isim):
    return f"Merhaba, {isim}!"  
# Parametre olarak 'isim' alsın.
# "Merhaba, [isim]!" şeklinde bir mesaj döndürsün (return).
# İpucu: def selamla(isim): ile başla

def selamla(isim):
    return f"Merhaba, {isim}!"

# GÖREV 2: Yazdığın fonksiyonu çağır ve "Ali" ismini parametre olarak ver.
# Sonucu bir değişkene ata ve ekrana yazdır.

sonuc = selamla("Ali")
print(sonuc)

# --- BÖLÜM 2: HESAPLAMA FONKSİYONU ---

# GÖREV 3: 'puan_donustur' adında bir fonksiyon yaz.
# Parametre: imdb_puani (10 üzerinden bir sayı, örn: 8.5)
# İşlem: Bu puanı 5 üzerinden hesapla (imdb_puani / 2)
# Return: Yeni puanı döndür

def puan_donustur(imdb_puani):
    return imdb_puani / 2   
# GÖREV 4: Bu fonksiyonu 8.5 ile çağır ve sonucu ekrana yazdır.

sonuc = puan_donustur(8.5)
print(sonuc)

# --- BÖLÜM 3: LİSTE İŞLEYEN FONKSİYON ---

# GÖREV 5: 'en_yuksek_puan' adında bir fonksiyon yaz.
# Parametre: filmler (bir liste, içinde sözlükler var)
# İşlem: Listedeki en yüksek puanlı filmi bul
# Return: En yüksek puanlı filmin adını döndür
# İpucu: for döngüsü kullanman gerekecek

filmler = [
    {"ad": "Inception", "puan": 8.8},
    {"ad": "The Matrix", "puan": 8.7},
    {"ad": "Interstellar", "puan": 8.6}
]

# Fonksiyonunu buraya yaz:
def en_yuksek_puan(filmler):
    en_yuksek = filmler[0]
    for film in filmler:
        if film["puan"] > en_yuksek["puan"]:
            en_yuksek = film
    return en_yuksek["ad"]



# GÖREV 6: Fonksiyonu çağır ve sonucu yazdır.

sonuc = en_yuksek_puan(filmler)
print(sonuc)

# --- BİTTİ Mİ? ---
# Terminale 'python odev_2_fonksiyonlar.py' yaz ve çalıştır!


