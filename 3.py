sayac=0

for i in dir(""):
    if "_" not in i[0]:
        sayac +=1
        print(i)

print("Toplam {} adet metod ile ilgileniyruz.".format(sayac))