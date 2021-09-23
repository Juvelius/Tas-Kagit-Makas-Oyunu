import random
secenek = ["T","K","M"]
tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]

print("Taş(T), Kağıt(K), Makas(M) oyununa hoşgeldin, oyunu bitirmek için 'kapat' yazmalısın.")

while True:
    secim = input("Taş mı, kağıt mı yoksa makas mı?")
    pc_secim = random.choice(secenek)

    if secim == tas:
        if pc_secim == tas:
            print("Bilgisayar taş yaptı, durum Berabere!")
        elif pc_secim == kagit:
            print("Bilgisayar kağıt yaptı, Kaybettin!")
        else:
            print("Bilgisayar makas yaptı. Kazandın!")
    if secim == kagit:
        if pc_secim == tas:
            print("Bilgisayar taş yaptı, Kazandın!")
        elif pc_secim == kagit:
            print("Bilgisayar kağıt yaptı, durum Berabere!")
        else:
            print("Bilgisayar makas yaptı. Kaybettin!")
    if secim == makas:
        if pc_secim == tas:
            print("Bilgisayar taş yaptı, Kaybettin!")
        elif pc_secim == kagit:
            print("Bilgisayar kağıt yaptı, Kazandın!")
        else:
            print("Bilgisayar makas yaptı. durum Berabere!")
    if secim == 'kapat':
        print("Oynadığınız için teşekkürler, çıkış yapılıyor.")
        break


