import psutil
import requests
import time
import webbrowser

# GÜVENLİK UYARISI: GitHub'a yüklemeden önce kendi bilgilerinizi silin!
# Kendi bot token'ınızı ve Chat ID'nizi aşağıya yazın.
TOKEN = "BURAYA_KENDI_BOT_TOKENINIZI_YAZIN"
CHAT_ID = "BURAYA_KENDI_CHAT_ID_NUMARANIZI_YAZIN"

last_status = None
son_guncelleme_id = None
muzik_acik_mi = False

print("✅ Asistan başlatılıyor...")

# --- GEÇMİŞİ TEMİZLEME ADIMI ---
# Program açıldığında eski mesajların hepsini okundu sayıp yoksayıyoruz
try:
    baslangic_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    baslangic_cevap = requests.get(baslangic_url).json()
    if baslangic_cevap.get("result"):
        son_guncelleme_id = baslangic_cevap["result"][-1]["update_id"]
    print("🧹 Eski mesajlar temizlendi.")
except:
    pass

print("🚀 Sistem aktif! (Durdurmak istersen terminale tıklayıp Ctrl + C yapabilirsin)\n")

while True:
    # --------------------------------------------------
    # 1. GÖREV: BATARYA KONTROLÜ
    # --------------------------------------------------
    battery = psutil.sensors_battery()
    if battery:
        plugged = battery.power_plugged
        if last_status is None:
            last_status = plugged
            
        if last_status and not plugged:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": "⚠️ Bilgisayar şarjdan çıkarıldı!"})
            print("Uyarı gönderildi: Şarjdan çekildi.")
            
        last_status = plugged

    # --------------------------------------------------
    # 2. GÖREV: TELEGRAM'DAN KOMUT DİNLEME
    # --------------------------------------------------
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
        if son_guncelleme_id:
            url += f"?offset={son_guncelleme_id + 1}"
            
        cevap = requests.get(url, timeout=5).json()
        
        if cevap.get("result"):
            for guncelleme in cevap["result"]:
                son_guncelleme_id = guncelleme["update_id"]
                
                if "message" in guncelleme and "text" in guncelleme["message"]:
                    mesaj_metni = guncelleme["message"]["text"].strip().lower()
                    
                    if mesaj_metni == "/muzik":
                        # Eğer müzik daha önce AÇILMADIYSA aç
                        if not muzik_acik_mi:
                            print("🎵 Müzik açılıyor (Sadece 1 sekme)...")
                            # new=2 parametresi zorla yeni sekmede (pencere değil) açmasını söyler
                            webbrowser.open("https://music.youtube.com/watch?list=PLtnz2GGi9r-GGlX8FMWAzyMlVx4wrHbYY&shuffle=1", new=2)
                            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": "🎵 Playlist başlatıldı patron!"})
                            muzik_acik_mi = True
                        
                        # Eğer zaten açıksa uyarı ver, sekme açma!
                        else:
                            print("🎵 Müzik zaten açık, engellendi.")
                            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": "🎵 Müzik zaten çalıyor, fazladan sekme açmadım!"})
                            
    except Exception as e:
        pass # Hataları yoksay, döngü sessizce devam etsin

    # İşlemciyi yormamak için 3 saniye dinlen
    time.sleep(3)