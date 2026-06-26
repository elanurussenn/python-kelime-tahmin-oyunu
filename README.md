# Python Kelime Tahmin Oyunu

Bu proje, Python ile geliştirilmiş basit bir kelime tahmin oyunudur. Program rastgele bir kelime seçer, kullanıcıya bazı ipucu harfleri gösterir ve oyuncudan harf tahmini yapmasını ister.

## Projenin Amacı

Bu projenin amacı; Python'da döngüler, koşullu ifadeler, kullanıcıdan veri alma, string işlemleri, puanlama sistemi ve temel oyun mantığı konularında pratik yapmaktır.

## Özellikler

- Rastgele kelime seçimi
- İpucu harf sistemi
- Yanlış tahmin hakkı
- Sesli ve sessiz harflere göre puanlama
- Yanlış tahminde puan düşürme
- Kelime tamamlanınca yeni kelimeye geçme veya oyundan çıkma seçeneği
- Kullanıcının daha önce tahmin ettiği harfleri gösterme

## Kullanım

Projeyi çalıştırmak için terminal veya komut istemcisinde şu komutu yazabilirsiniz:

```bash
python kelime_tahmin_oyunu.py
```

Program çalıştıktan sonra ekrandaki yönergeleri takip ederek harf tahmininde bulunabilirsiniz.

## Oyun Kuralları

- Bilgisayar rastgele bir kelime seçer.
- Oyuncuya kelimenin uzunluğu gösterilir.
- Oyuncuya bazı ipucu harfleri verilir.
- Oyuncu tek tek harf tahmini yapar.
- Doğru tahmin edilen harfler kelime üzerinde açılır.
- Doğru tahminlerde puan kazanılır.
- Yanlış tahminlerde puan düşer.
- Yanlış tahmin hakkı biterse oyun sona erer.
- Kelime doğru tamamlanırsa oyuncu yeni kelimeye geçebilir veya oyundan çıkabilir.

## Puanlama Sistemi

- Doğru tahmin edilen sesli harfler daha yüksek puan kazandırır.
- Doğru tahmin edilen sessiz harfler puan kazandırır.
- Yanlış tahminlerde puan düşer.
- Hiç yanlış tahmin yapmadan kelime doğru bilinirse bonus puan kazanılır.

## Kullanılan Teknolojiler

- Python
- Random modülü
- Döngüler
- Koşullu ifadeler
- String işlemleri
- Kullanıcı girişi

## Dosya Yapısı

```txt
python-kelime-tahmin-oyunu/
│
├── kelime_tahmin_oyunu.py
└── README.md
```

## Not

Bu proje başlangıç seviyesi Python algoritma ve oyun mantığı pratiği için hazırlanmıştır.
