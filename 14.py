evet=0
hayir=0
for i in range(100):
    print("Turnuvaya katılım şartlarının hepsini yerine getiriyor musunuz evet ya da hayir şeklince vevap veriniz")
    cevap=input()
    if cevap=="evet":
        evet=evet+1
    if cevap=="hayir":
        hayir=hayir+1
print("turnuvaya katılanların sayısı", evet, " katılamayanların sayısı", hayir)
