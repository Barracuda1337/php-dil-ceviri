import re
import os
import time
from deep_translator import GoogleTranslator

# Ayarlar
input_file = "en_lang.php" # çevirilecek dosya adı
output_folder = "translated_parts" # parçalara bölerken kullanılacak klasör
final_output_file = "lang.tr.php" # işlem bittikten sonra kaydedilecek dosya adı
lines_per_part = 500 # parça başına satır sayısı
source_lang = "en" # ana dil dosya dil
target_lang = "tr" # çevirilecek hedef dil en -> tr
max_retries = 3 # rate limit olması halinde max deneme sayısı
retry_delay = 2  # saniye

# Hazırlık
translator = GoogleTranslator(source=source_lang, target=target_lang)
os.makedirs(output_folder, exist_ok=True)

def translate_with_retry(text, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            translated = translator.translate(text)
            time.sleep(0.5)  # Her çeviri arasında 0.5 saniye bekle
            return translated
        except Exception as e:
            if attempt == max_attempts - 1:  # Son deneme
                print(f"Çeviri hatası (son deneme): {e}")
                return text
            print(f"Çeviri hatası (deneme {attempt + 1}/{max_attempts}): {e}")
            time.sleep(retry_delay)  # Hata durumunda daha uzun bekle
    return text

with open(input_file, 'r', encoding='utf-8') as f:
    all_lines = f.readlines()

part_counter = 1
translated_part_files = []
current_part = []
total_lines = len(all_lines)

for i, line in enumerate(all_lines):
    match = re.match(r'(.*\$lang\[\s*["\'].*?["\']\s*\]\s*=\s*")(.+?)(";.*)', line)
    if match:
        prefix, value, suffix = match.groups()
        translated_text = translate_with_retry(value)
        line = f'{prefix}{translated_text}{suffix}\n'
    
    current_part.append(line)

    # İlerleme durumunu göster
    if (i + 1) % 10 == 0:  # Her 10 satırda bir ilerleme göster
        print(f"İşleniyor: {i + 1}/{total_lines} satır ({(i + 1)/total_lines*100:.1f}%)")

    # 500 satıra ulaşınca bir dosya yaz
    if len(current_part) == lines_per_part or i == len(all_lines) - 1:
        part_file = os.path.join(output_folder, f'translated_part_{part_counter}.php')
        with open(part_file, 'w', encoding='utf-8') as pf:
            pf.writelines(current_part)
        translated_part_files.append(part_file)
        current_part = []
        part_counter += 1
        print(f"Parça {part_counter-1} kaydedildi. 5 saniye bekleniyor...")
        time.sleep(5)  # Her parça arasında 5 saniye bekle

# Parçaları birleştir
print("\nParçalar birleştiriliyor...")
with open(final_output_file, 'w', encoding='utf-8') as final_file:
    for part in translated_part_files:
        with open(part, 'r', encoding='utf-8') as pf:
            final_file.writelines(pf.readlines())

print(f"\n✅ Çeviri tamamlandı: {final_output_file}")
