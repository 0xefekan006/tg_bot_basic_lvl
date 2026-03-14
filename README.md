# 🤖 Telegram Mac Asistanı (Batarya & Müzik Botu)

Bu proje, macOS (veya Windows/Linux) bilgisayarınızın batarya durumunu arka planda takip eden ve Telegram üzerinden verdiğiniz komutlarla bilgisayarınızı uzaktan kontrol etmenizi sağlayan hafif bir Python asistanıdır.

## 🌟 Özellikler

* **🔋 Batarya Takibi:** Bilgisayarınız şarjdan çıkarıldığında anında Telegram üzerinden uyarı mesajı gönderir.
* **🎵 Uzaktan Müzik Kontrolü:** Telegram'dan `/muzik` komutunu gönderdiğinizde, bilgisayarınızda otomatik olarak YouTube Music açılır ve favori çalma listeniz karışık (shuffle) modda çalmaya başlar.
* **🛡️ Sekme Koruması (Anti-Spam):** Müziği birden fazla kez açmaya çalışırsanız, asistan bunu algılar ve onlarca sekme açılmasını önlemek için işlemi engeller.
* **🧹 Başlangıç Temizliği:** Program ilk başlatıldığında eski komutları yoksayar, sadece o anki güncel komutlara yanıt verir.

## 🛠️ Kurulum ve Ayarlar

Bu asistanı kendi bilgisayarınızda çalıştırmak için aşağıdaki basit adımları izleyebilirsiniz.

### 1. Gereksinimler
Bilgisayarınızda Python 3'ün yüklü olduğundan emin olun. Projenin çalışması için gereken kütüphaneleri terminale şu komutu yazarak kurun:
```bash
pip3 install psutil request 


2- 
TOKEN = "BURAYA_KENDI_BOT_TOKENINIZI_YAZIN"
CHAT_ID = "BURAYA_KENDI_CHAT_ID_NUMARANIZI_YAZIN"

3. Çalıştırma
Terminal (veya Komut İstemcisi) üzerinden projenin bulunduğu klasöre gidin ve botu başlatın:
python3 github_bot.py