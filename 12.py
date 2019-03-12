toplam=0
while True:
    sayi=int(input("0 ile 100 arasında sayı ve ya sayılar giriniz"))
    toplam=toplam+sayi
    if sayi<0 or sayi>100:
        print("girdiğiniz sayı 0 ie 100 arasında olmalıydı")
        break
print(toplam) 
