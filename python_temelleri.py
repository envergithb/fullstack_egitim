# Modül 2: Python Temelleri - Veri Yapıları
# Konu: Film Verisini Modelleme

# 1. Değişkenler (Variables)
# Bir veriyi saklamak için kullandığımız isimlendirilmiş kutulardır.
film_adi = "Inception"  # String (Metin)
yapim_yili = 2010       # Integer (Tam Sayı)
imdb_puani = 8.8        # Float (Ondalıklı Sayı)
izlendi_mi = True       # Boolean (Mantıksal Değer)

print(f"Film: {film_adi} ({yapim_yili}) - Puan: {imdb_puani}")

# 2. Listeler (Lists)
# Birden fazla veriyi tek bir yerde tutmak için kullanılır. Sıralıdır ve değiştirilebilir.
# Örnek: Bir filmin oyuncularını tutalım.
oyuncular = ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]

print("\nOyuncular:")
print(oyuncular[0])  # İlk eleman (0. indeks)
print(oyuncular[-1]) # Son eleman

# Listeye yeni eleman ekleme
oyuncular.append("Tom Hardy")
print(f"Güncel Oyuncu Sayısı: {len(oyuncular)}")

# 3. Sözlükler (Dictionaries) - EN ÖNEMLİSİ
# Verileri "Anahtar: Değer" (Key: Value) çiftleri halinde tutar.
# Gerçek hayattaki bir nesneyi (Film, Kullanıcı, Ürün) modellemek için mükemmeldir.

film_detay = {
    "baslik": "Inception",
    "yil": 2010,
    "puan": 8.8,
    "yonetmen": "Christopher Nolan",
    "oyuncular": oyuncular, # Listeyi sözlük içinde kullanabiliriz!
    "vizyonda_mi": False
}

print("\nFilm Detayı (Sözlük):")
print(film_detay)
print(f"Yönetmen: {film_detay['yonetmen']}")

# 4. Listeler İçinde Sözlükler (JSON Yapısına Hazırlık)
# Birden fazla filmi tutmak isterseniz, sözlüklerden oluşan bir liste yaparsınız.
# Bu yapı, veritabanından veya API'den gelen verinin aynısıdır.

filmler = [
    {
        "id": 1,
        "baslik": "Inception",
        "puan": 8.8
    },
    {
        "id": 2,
        "baslik": "The Matrix",
        "puan": 8.7
    },
    {
        "id": 3,
        "baslik": "Interstellar",
        "puan": 8.6
    }
]

print("\nFilm Listesi:")
for film in filmler:
    print(f"{film['baslik']} filminin puanı: {film['puan']}")
