# PHP Dil Dosyası Çeviri Aracı

Bu araç, PHP dil dosyalarını otomatik olarak çevirmek için geliştirilmiş bir Python betiğidir. Google Translate API'sini kullanarak İngilizce'den Türkçe'ye (veya diğer dillere) çeviri yapabilir.

## 🚀 Özellikler

- PHP dil dosyalarını otomatik çevirme
- Google Translate API entegrasyonu
- Büyük dosyaları parçalara bölerek işleme
- Hata yönetimi ve yeniden deneme mekanizması
- İlerleme göstergesi
- Rate limiting koruması

## 📋 Gereksinimler

- Python 3.x
- deep-translator kütüphanesi
- requests kütüphanesi

## 🔧 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/Barracuda1337/php-dil-ceviri.git
cd php-dil-ceviri
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install deep-translator
```

## 💻 Kullanım

1. Çevirmek istediğiniz PHP dil dosyasını proje dizinine kopyalayın
2. `index.py` dosyasındaki ayarları düzenleyin:
```python
input_file = "en_lang.php"  # Giriş dosyası
output_folder = "translated_parts"  # Parça dosyalarının kaydedileceği klasör
final_output_file = "lang.tr.php"  # Çıktı dosyası
source_lang = "en"  # Kaynak dil
target_lang = "tr"  # Hedef dil
```

3. Betiği çalıştırın:
```bash
python index.py
```

## 📝 Desteklenen Format

Betik, aşağıdaki formattaki PHP dil dosyalarını destekler:

```php
$lang["key"] = "value";
// veya
$lang['key'] = "value";
```

## ⚙️ Ayarlar

- `lines_per_part`: Her parçada işlenecek satır sayısı (varsayılan: 500)
- `max_retries`: Başarısız çeviriler için maksimum deneme sayısı (varsayılan: 3)
- `retry_delay`: Yeniden denemeler arasındaki bekleme süresi (saniye)

## ⚠️ Önemli Notlar

- Google Translate API'si ücretsiz kullanımda sınırlamalara sahiptir
- Çok büyük dosyalar için işlem süresi uzun olabilir
- Çeviri kalitesi Google Translate'in kalitesine bağlıdır

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Bir Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## 👥 İletişim

Sorularınız veya önerileriniz için bir issue açabilirsiniz.

---
⭐️ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! 
