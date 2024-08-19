import random

def tas_kagit_makas_ElifBerra_Gonul():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyunun kuralları:")
    print("-Oyuncu ve bilgisayar sırayla taş, kağıt, ya da makası seçer.")
    print("-İki galibiyete ulaşan oyunu kazanır.")
    print("Oyun bittiğinde tekrar oynamak isteyip istemediğiniz sorulacaktır.")

    secenekler = ["taş", "kağıt", "makas"]
    toplam_oyun_sayisi = 0
    oyun_devam = True

    # Oyunun başlangıç yeri
    while oyun_devam:
        tur = 0
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        toplam_oyun_sayisi += 1

        # Biri 2 galibiyete ulaşana kadar devam eden döngü
        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            print(
                f"\nOyun {toplam_oyun_sayisi} - Galibiyetler: Oyuncu {oyuncu_galibiyet}, Bilgisayar {bilgisayar_galibiyet}")
            tur += 1

            # Oyuncu seçimi al
            oyuncu_secim = input("Taş, kağıt ya da makası seçin: ").lower()
            if oyuncu_secim not in secenekler:
                print("Geçersiz bir seçim yaptınız. Lütfen taş, kağıt ya da makası seçiniz.")
                continue

            # Bilgisayar seçimi
            bilgisayar_secim = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            # Beraberlik durumu
            if oyuncu_secim == bilgisayar_secim:
                print("Beraberlik!")

            # Oyuncunun kazanma durumu
            elif (oyuncu_secim == "taş" and bilgisayar_secim == "makas") or \
                    (oyuncu_secim == "kağıt" and bilgisayar_secim == "taş") or \
                    (oyuncu_secim == "makas" and bilgisayar_secim == "kağıt"):
                print("Tur sonucu: Oyuncu kazandı!")
                oyuncu_galibiyet += 1

            # Bilgisayarın kazanma durumu
            else:
                print("Tur sonucu: Bilgisayar kazandı!")
                bilgisayar_galibiyet += 1

            print(f"Toplam tur sayısı: {tur}")

        # Oyunun galibini belirleme
        if oyuncu_galibiyet == 2:
            print("\nOyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı!")

        # Yeni oyun başlatma veya oyunu bitirme
        print("Tekrar oynamak ister misiniz?")
        yeniden_oyna = input("Seçiminizi yapın (evet/hayır): ").lower()

        if yeniden_oyna == "hayır":
            oyun_devam = False
            print("Oyun sona erdi.")
        elif yeniden_oyna != "evet":
            print("Geçersiz seçim. Oyun sona erdi.")
            oyun_devam = False
