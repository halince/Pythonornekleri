toplam=0
for i in range(10):
    print(i+1, " inci sayıyı giriniz")
    sayi=int(input())
    toplam=toplam+sayi
print("girdiğiniz sayıların toplamı=",toplam)
print("girdiğiniz sayıların ortalaması",toplam/10)
