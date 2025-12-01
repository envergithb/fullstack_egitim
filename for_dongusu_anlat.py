# FOR DÖNGÜSÜ NEDİR?
# Bir listedeki her elemanı tek tek işlemek için kullanılır.

# GERÇEK HAYAT ÖRNEĞİ:
# Elinde bir sepet portakal var. Her portakalı tek tek alıp tartıyorsun.
# For döngüsü de aynen böyle çalışır.

# --- ÖRNEK 1: BASİT LİSTE ---
print("=== ÖRNEK 1: İsimleri Yazdır ===")
isimler = ["Ali", "Ayşe", "Mehmet"]

# "isimler" listesindeki her eleman için:
for isim in isimler:
    print(isim)

# Çıktı:
# Ali
# Ayşe
# Mehmet

# AÇIKLAMA:
# "for isim in isimler:" demek:
# "isimler listesindeki her bir elemanı al, ona 'isim' de, ve aşağıdaki kodu çalıştır"

print("\n=== ÖRNEK 2: Sayılarla İşlem ===")
sayilar = [10, 20, 30]

for sayi in sayilar:
    sonuc = sayi * 2
    print(f"{sayi} x 2 = {sonuc}")

# Çıktı:
# 10 x 2 = 20
# 20 x 2 = 40
# 30 x 2 = 60

# --- ÖRNEK 3: SÖZLÜKLERLE (FİLM ÖRNEĞİ) ---
print("\n=== ÖRNEK 3: Film Listesi ===")
filmler = [
    {"ad": "Matrix", "puan": 8.7},
    {"ad": "Inception", "puan": 8.8},
    {"ad": "Interstellar", "puan": 9.0}
]

# Her film için:
for film in filmler:
    print(f"{film['ad']} filminin puanı: {film['puan']}")

# Çıktı:
# Matrix filminin puanı: 8.7
# Inception filminin puanı: 8.8
# Interstellar filminin puanı: 9.0

# --- ÖRNEK 4: EN YÜKSEK PUANI BULMA (GÖREV 5 İÇİN) ---
print("\n=== ÖRNEK 4: En Yüksek Puanlı Film ===")

# Başlangıçta en yüksek puanı 0 kabul edelim
en_yuksek_puan = 0
en_iyi_film = ""

# Her filmi kontrol et
for film in filmler:
    # Eğer bu filmin puanı, şu ana kadarki en yüksek puandan büyükse:
    if film["puan"] > en_yuksek_puan:
        # Yeni en yüksek puanı güncelle
        en_yuksek_puan = film["puan"]
        en_iyi_film = film["ad"]

print(f"En yüksek puanlı film: {en_iyi_film} ({en_yuksek_puan})")

# --- ALIŞTIIRMA ---
print("\n=== ALIŞTIRMA: Şimdi Sen Dene ===")
# Aşağıdaki listedeki tüm sayıları topla ve ekrana yazdır.
# İpucu: Başta toplam = 0 yap, döngüde her sayıyı toplama ekle.

sayilar = [5, 10, 15, 20]

# Buraya kodunu yaz:

for sayi in sayilar:
    toplam =+ sayi
    
print(toplam)