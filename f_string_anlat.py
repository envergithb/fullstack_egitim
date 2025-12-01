# F-STRING (FORMATTED STRING) NEDİR?
# Değişkenleri metin içine yerleştirmenin en kolay yolu.

# --- ESKI YÖNTEM (Kullanma!) ---
isim = "Ali"
yas = 25

# Eski yöntem: Virgülle ayırma
print("Merhaba", isim, "yaşın", yas)
# Çıktı: Merhaba Ali yaşın 25
# Sorun: Boşluklar garip, okunması zor

# --- YENİ YÖNTEM: F-STRING ---
print(f"Merhaba {isim}, yaşın {yas}")
# Çıktı: Merhaba Ali, yaşın 25
# Avantaj: Okuması kolay, tam istediğin gibi

# F-STRING NASIL ÇALIŞIR?
# 1. Tırnak işaretinden önce 'f' harfi koy
# 2. Değişkenleri süslü parantez {} içine yaz

# --- ÖRNEKLER ---

film = "Matrix"
puan = 8.7

# Örnek 1: Basit kullanım
print(f"{film} filminin puanı {puan}")
# Çıktı: Matrix filminin puanı 8.7

# Örnek 2: Matematiksel işlem
print(f"{film} filminin 5 üzerinden puanı: {puan / 2}")
# Çıktı: Matrix filminin 5 üzerinden puanı: 4.35

# Örnek 3: Sözlükten veri
film_detay = {"ad": "Inception", "yil": 2010}
print(f"{film_detay['ad']} filmi {film_detay['yil']} yılında çıktı")
# Çıktı: Inception filmi 2010 yılında çıktı

# --- F-STRING OLMADAN NASIL OLURDU? ---
# Çok karmaşık ve okunması zor:
print(film_detay['ad'] + " filmi " + str(film_detay['yil']) + " yılında çıktı")
# Aynı çıktı ama kod çok çirkin!

# --- ÖZET ---
# f"Metin {degisken} metin" = Değişkeni metin içine yerleştir
# Süslü parantez {} içindeki her şey Python kodu olarak çalışır

# ALIŞTIRMA:
# Aşağıdaki değişkenleri kullanarak bir cümle yaz:
ad = "Ahmet"
sehir = "İstanbul"
meslek = "Mühendis"

# Hedef çıktı: "Ahmet İstanbul'da yaşayan bir Mühendis"
# Buraya kodunu yaz (f-string kullan):
