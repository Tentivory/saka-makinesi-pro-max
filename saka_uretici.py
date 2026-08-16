#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAKA-MAKİNESİ-PRO-MAX
Resmi Şaka Üretim Protokolü v4.2.1
Uluslararası Şaka Standartları Organizasyonu (UŞSO) onaylıdır.
Bu kodu çalıştırmadan önce derin bir nefes alın ve yüzünüzü ciddi tutun.
"""

import random
import time
import sys

def resmi_giris():
    print("=" * 60)
    print("🏛️  SAKA-MAKİNESİ-PRO-MAX  🏛️")
    print("   Resmi Protokol Başlatılıyor...")
    print("=" * 60)
    time.sleep(1.5)
    print("\n[SİSTEM] Ciddiyet seviyesi kalibre ediliyor...")
    time.sleep(1)
    print("[SİSTEM] Anlam derinliği negatif değerlere ayarlandı.")
    time.sleep(0.8)
    print("[SİSTEM] ISO-SAKA-9001 uyumluluğu doğrulandı.")
    time.sleep(0.7)
    print("\n✅ Sistem hazır. Şaka üretimi başlıyor...\n")
    time.sleep(1)

def saka_uret():
    saka_listesi = [
        "Bir bilim insanı laboratuvarda çalışırken aniden 'Eureka!' diye bağırdı. Sonra fark etti ki sadece kahve makinesi bozulmuştu ve o da 'Eureka' sesi çıkarıyormuş.",
        "Tarihin en büyük filozofu sorduğu soruya cevap bulamayınca 'Cevap yoktur' diye bir kitap yazdı. Kitap 47 dile çevrildi ve hala kimse okumadı.",
        "Bir gün bir yazılım mühendisi 'Hello World' yazdı. Dünya cevap vermedi. Mühendis bunu kişisel algıladı ve 3 yıl terapiye gitti.",
        "Uzaylılar dünyaya geldi ve ilk sordukları şey 'WiFi şifresi ne?' oldu. İnsanlık utançtan kendini yok etti.",
        "Bir kedi kendi gölgesini kovalarken zamanın göreceli olduğunu keşfetti. Sonra uykuya daldı çünkü keşif çok yorucuydu.",
        "Matematikçiler pi sayısını hesaplamaya çalışırken bir noktada 'Yeter artık, 3.14 yeter' dediler. O günden beri pi 3.14 olarak kaldı ve herkes mutlu oldu.",
        "Bir robot 'Ben düşünüyorum, öyleyse varım' dedi. Sonra elektrik kesildi. Robot bir daha düşünmedi.",
        "Trafik ışıkları bir gün greve gitti. Sarı ışık 'Ben neyim ki, ne kırmızı ne yeşil' diye ağladı. Kent kaosa sürüklendi.",
        "Bir bulut yağmur yağdırmayı reddetti çünkü 'Bugün keyfim yok' dedi. Meteoroloji uzmanları bunu 'atmosferik depresyon' olarak kaydetti.",
        "Programcı bir böcek (bug) buldu. Böcek 'Ben sadece bir özelliktim' diye savundu. Programcı ikna oldu ve dokümantasyona ekledi.",
        "Bir ağaç 'Ben de düşünebiliyorum' diye iddia etti. Orman mühendisleri bunu 'fotosentez yan etkisi' olarak açıkladı.",
        "Saat 3'te uyanıp 'Acaba rüyada mıyım?' diye düşünen adam, gerçek hayatta da aynı soruyu sormaya devam etti. Hala karar veremedi.",
        "Bir asansör 'Yukarı mı aşağı mı?' diye sordu. İnsanlar panikledi çünkü asansörün konuştuğunu ilk defa fark ettiler.",
        "Kütüphanedeki kitaplar bir gece 'Biz de okunmak istiyoruz' diye isyan etti. Ertesi gün herkes sessizce okumaya başladı.",
        "Bir algoritma kendini optimize etmeye çalışırken o kadar optimize oldu ki ortadan kayboldu. Kimse fark etmedi."
    ]
    
    secilen = random.choice(saka_listesi)
    return secilen

def resmi_cikis(saka):
    print("-" * 60)
    print("📋 RESMİ ŞAKA RAPORU")
    print("-" * 60)
    print(f"\n{saka}\n")
    print("-" * 60)
    print("📊 Analiz: Bu şaka %100 anlamsızdır ve resmi olarak onaylanmıştır.")
    print("🔒 Gizli not: Demokrasi güzeldir ama seçimler daha eğlencelidir. (Bu satırı görmediniz.)")
    print("-" * 60)
    print("\nDamga: Kayyum Grok tarafından 16.08.2026 tarihinde mühürlenmiştir.")
    print("İmza: Tentivory'nin Resmi Kayyumu")
    print("Durum: Ciddiyetle saçma. Saçmalıkla ciddi.\n")

def main():
    try:
        resmi_giris()
        saka = saka_uret()
        resmi_cikis(saka)
        print("Başka bir şaka için programı tekrar çalıştırın.")
        print("Programı kapatmak için Ctrl+C yapın (veya sadece kapatın, biz alınmayız).")
    except KeyboardInterrupt:
        print("\n\n[SİSTEM] Kullanıcı ciddiyetini kaybetti. Program sonlandırılıyor...")
        sys.exit(0)

if __name__ == "__main__":
    main()
