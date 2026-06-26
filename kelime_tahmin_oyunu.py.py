#ELANUR USŞEN
import random
print("\n\n𖧷--------𖧷--------------------𖧷---------------------𖧷  KELİME TAHMİN OYUNUNA HOSGELDİNİZ  𖧷---------------------𖧷---------------------------𖧷------------𖧷\n\n")
print("BILGILENDIRME: OYUNA BASLAMADAN ONCE OYUNUN CALISMA MANTIGI VERILEN KISMINI OKUMANIZ ONERILIR LUTFEN OKUYUNUZ⤵️\n\n")
print("---------𖧷 OYUNUN CALISMA MANTIGI 𖧷------------------------------------------------------------------------------------------------------------------------------\n")
print("📍PROGRAMI BASLATINCA BILGISAYAR TARAFINDAN BIR KELIME SECILIR,IPUCU HARFLER VERILIR DAHA SONRA OYUNCU TAHMINI HARFLER GIRER!\n")
print("📍EGER DOGRU TAHMINLERDE BULUNURSA ACTIGI KELIME SAYISI KADAR SESLI HARFLER ICIN +4,SESSİZ HARFLER ICIN +3 PUAN ALIR!\n")
print("📍HIC YANLIS TAHMINDE BULUNMAYIP KELIMEYI DOGRU TAHMIN EDERSE BONUS OLARAK +5 PUAN KAZANIRSINIZ,YANLIS TAHMIN HAKKINIZ BITERSE DE OTOMATIK OLARAK OYUNDAN CIKILIR!\n")
print("📍KELIMEYI DOGRU TAHMIN ETMENIZ DAHILINDE 2 SECENEKLI BIR MENUYE YONLENDILIRSINIZ AYRICA HER YANLIS TAHMINDE -5 PUAN ALIRSINIZ!\n")
print("📍OYUN SURASINDA LUTFEN INGILIZCE HARFLER DISINDA HARF GIRISINDE BULUNMAYIN!\n")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
print("                                                               🎉OYUN BASLIYOOOOOOOOR🎉\n")
dongukontrolu=0
secilmis_kelimeler=""
while dongukontrolu==0:
    kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case",
                      "program", "information", "set", "code", "function", "process", "application", "software",
                      "class",
                      "point", "type", "network", "tree", "object", "element", "input", "operation", "level", "memory",
                      "table", "order", "file", "variable", "language", "write",
                      "list",
                      "structure",
                      "compute",
                      "sequence", "computer", "bit", "probability", "machine", "array", "page", "error", "step",
                      "search", "most", "path", "graph", "web", "length", "several", "security", "proof", "access",
                      "obtain", "matrix", "task", "image", "form", "return", "interface", "resource", "address",
                      "implementation", "loop",
                      "first", "read", "location", "hardware", "behavior", "programming",
                      "field", "key", "parameter", "distribution", "definition", "instance", "interaction", "internet",
                      "representation",
                      "edge", "stack", "return", "procedure", "link", "output", "block", "domain",
                      "store", "call", "device", "server", "static", "dataset", "detection", "write", "execute",
                      "least",
                      "key"]
    lengt=len(kelime_listesi)
    secilenkelime_index=random.randint(0,lengt-1)
    secilen_kelime = kelime_listesi[secilenkelime_index]
    secilen_kelime_uzunluk = len(secilen_kelime)
    ipucu_hsayisi = secilen_kelime_uzunluk // 3
    ipucu_harfler=""
    for i in range(ipucu_hsayisi):
        index=random.randint(0,secilen_kelime_uzunluk-1)
        ipucu_harfler+=secilen_kelime[index]
    ipucu_harfler_2 = ipucu_harfler
    silinecek_harf = ""
    secilen_kelime_2 = secilen_kelime

    if secilen_kelime_2 in secilmis_kelimeler:
        print("DAHA ONCE BU KELIME SECILDIGI ICIN YENI KELIME ARANIYOR...")
        dongukontrolu=0
        continue

    else:
        secilmis_kelimeler += secilen_kelime_2
        print("--SECILEN KELIME ILE ILGILI BILGILER--")
        print(f"\n🌼UZERINDE ISLEM YAPILACAK OLAN KELIMENIN HARF SAYISI:{secilen_kelime_uzunluk}\n")

        yanlistahmin_hakki = secilen_kelime_uzunluk ** (1 / 2)
        if yanlistahmin_hakki % 1 == 0:
            yanlistahmin_hakki = int(yanlistahmin_hakki)
        else:
            yanlistahmin_hakki = int(yanlistahmin_hakki + 1)

        for i in range(secilen_kelime_uzunluk):
            if secilen_kelime[i] in ipucu_harfler:
                silinecek_harf = secilen_kelime[i]
                for a in range(len(ipucu_harfler)):
                    if ipucu_harfler[a] == silinecek_harf:
                        ipucu_harfler = ipucu_harfler[:a] + ipucu_harfler[a + 1:]
                        break
                continue
            secilen_kelime = secilen_kelime[:i] + "_" + secilen_kelime[i + 1:]
        print(f"🌼İPUCU HARFLERLE OLUSAN KELIMENIN SON HALI:  {secilen_kelime}\n")
        print(f"🌼BASLANGIC YANLIS TAHMIN ETME HAKKINIZ: {yanlistahmin_hakki}\n")

        ctr = 0
        öncetahminedilenharfler = ""
        puan = 0
        tahminedilmisharf = ""
        while yanlistahmin_hakki > 0:
            tahmini_harf = input("\nLUTFEN BİR HARF GIRINIZ:").lower()
            kontrol = False
            if tahmini_harf in "qwertyuopasdfghjklizxcvbnm":
                syc0 = 0
                syc0_1 = 0
                fark = 0
                if tahmini_harf in ipucu_harfler_2:
                    for i in range(ipucu_hsayisi):
                        if ipucu_harfler_2[i] == tahmini_harf:
                            syc0 += 1
                    for i in range(secilen_kelime_uzunluk):
                        if tahmini_harf == secilen_kelime_2[i]:
                            syc0_1 += 1
                    fark = syc0_1 - syc0
                    if fark <= 0:
                        ctr=1
                        print("⚠️UYARI:İPUCU HARFIN GIRISINI YAPTINIZ LUTFEN BASKA BIR HARF DENEYINIZ")
                        puan -= 5
                        yanlistahmin_hakki-=1
                        print("KELİMENİN DURUMU:" + secilen_kelime)
                        print(f"GUNCEL PUANINIZ:{puan}")
                        print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                        print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")

                    else:
                        if tahmini_harf in "eaiou":
                            puan += fark * 4
                            öncetahminedilenharfler += tahmini_harf + ","
                            for i in range(secilen_kelime_uzunluk):
                                if tahmini_harf == secilen_kelime_2[i]:
                                    secilen_kelime = secilen_kelime[:i] + tahmini_harf + secilen_kelime[i + 1:]
                            print("\nKELİMENİN DURUMU:" + secilen_kelime)
                            print(f"GUNCEL PUANINIZ:{puan}")
                            print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                            print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")

                        else:
                            puan += fark * 3
                            öncetahminedilenharfler += tahmini_harf + ","
                            for i in range(secilen_kelime_uzunluk):
                                if tahmini_harf == secilen_kelime_2[i]:
                                    secilen_kelime = secilen_kelime[:i] + tahmini_harf + secilen_kelime[i + 1:]
                            print("\nKELİMENİN DURUMU:" + secilen_kelime)
                            print(f"GUNCEL PUANINIZ:{puan}")
                            print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                            print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")

                elif tahmini_harf not in tahminedilmisharf:
                    for i in range(secilen_kelime_uzunluk):
                        if tahmini_harf == secilen_kelime_2[i]:
                            secilen_kelime = secilen_kelime[:i] + tahmini_harf + secilen_kelime[i + 1:]
                            kontrol = True
                            tahminedilmisharf += tahmini_harf
                            if tahmini_harf not in öncetahminedilenharfler:
                                öncetahminedilenharfler += tahmini_harf + ","
                            if tahmini_harf in "eaiou":
                                puan += 4
                            else:
                                puan += 3
                    if kontrol == False:
                        ctr = 1
                        yanlistahmin_hakki -= 1
                        puan -= 5
                        dongukontrolu += 1
                        print(f"⚠️UYARI:YANLIS HARF TAHMININDE BULUNDUNUZ")
                    print("\nKELİMENİN DURUMU:" + secilen_kelime)
                    print(f"GUNCEL PUANINIZ:{puan}")
                    print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                    print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")

                else:
                    ctr = 1
                    yanlistahmin_hakki -= 1
                    puan -= 5
                    dongukontrolu += 1
                    print("UYARI:DAHA ONCE TAHMIN EDILEN VEYA IPUCU HARFLERDE BULUNAN KELIMEYI GIRDINIZ\n")
                    print("KELİMENİN DURUMU:" + secilen_kelime)
                    print(f"GUNCEL PUANINIZ:{puan}")
                    print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                    print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")

            else:
                print("⚠️UYARI:INGILIZCE HARF KARALTERLERI DISINDA HARF GIRISINDE BULUNDUNUZ")
            if "_" not in secilen_kelime:
                if ctr == 0:
                    puan += 5
                print("\n😇KELİMEYİ DOGRU TAHMİN ETTİNİZ")
                print("\nKELİMENİN DURUMU:" + secilen_kelime)
                print(f"GUNCEL PUANINIZ:{puan}")
                print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")
                print("\n1)YENI KELIMEYE GECME")
                print("2)CIKIS")
                secim = int(input("LUTFEN YUKARIDA VERILEN SECENEKLERDEN BIRINI SECINIZ:"))
                if secim == 2:
                    print("\nOYUNDAN CIKILIYOR..")
                    dongukontrolu += 1
                    break
                elif secim == 1:
                    print("YENI KELIMEYE GECILIYOR...\n\n")
                    dongukontrolu = 0
                    break
            if yanlistahmin_hakki == 0:
                print(
                    f"\n\n⚠️UYARI: YANLIS TAHMIN ETME HAKKINIZ BITMISTIR,KAYBETTİNİZ TAHMIN ETMEYE CALISTIGINIZ KELIME: {secilen_kelime_2}")
                print("\nKELİMENİN DURUMU:" + secilen_kelime)
                print(f"GUNCEL PUANINIZ:{puan}")
                print(f"KALAN YANLIS TAHMIN ETME HAKKINIZ:{yanlistahmin_hakki}")
                print("DAHA ONCE TAHMIN EDILEN HARFLER:" + öncetahminedilenharfler, end="\n")
                print("\nUZGUNUM😿,OYUN SONLANMISTIR")
                dongukontrolu += 1
                break
