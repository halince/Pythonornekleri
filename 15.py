evet=0
hayir=0
for i in range(100):
    print("Turnuvaya katılım şartlarının hepsini yerine getiriyor musunuz evet ya da hayir şeklince vevap veriniz")
    cevap=input()
    if cevap=="evet":
        evet=evet+1
        if evet==50:
            print(" turnuvaya katılımcı sayısı", evet," e ulaşmıştır. toplam katılımcı sayısı",evet+hayir)
            break
    if cevap=="hayir":
        hayir=hayir+1
