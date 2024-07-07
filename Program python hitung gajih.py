import time

name=input("Nama :")
print("Masukkan jam dalam format 24 jam")
masuk=input("Jam masuk kerja :")
keluar=input("Jam keluar kerja :")

jamasuk=masuk.split(".")
jamkeluar=keluar.split(".")
#split antara jam dan menit
menit1 = jamasuk[1]
menit2 = jamkeluar[1]
#kegunaan split untuk perhitungan menit
total1 = int(menit1) + int(menit2)
#penambahan kedua variabel untuk menit untuk perhitungan total
totalmenit = int(total1)/60
#bila menit >60 akan dimasukkan ke perhitungan total 

jamawal= jamasuk[0]
jambelakang= jamkeluar[0]
total =int(jambelakang)-int(jamawal)+int(totalmenit)
if (total > 0) :
    print("---------------rincian gaji----------------")
    print("Nama         :", name)
    print("Waktu Kerja  :",total,"jam", "[",masuk,"sd",keluar,"]")
    print("Gaji perhari : Rp 175000")
    print("\n")

    if(total>8):
        lembur = (int(total)-8)*15000
        print("lembur       :Rp",lembur,'Dari [',(total-8),"] jam x Rp 15000")
        print("\n")
        print("Total Gaji   :Rp", int(lembur) + 175000)
    else:
        print("Lembur       : TIDAK ADA LEMBUR")


else:
    print("Anda tidak kerja dan gaji akan dipotong ")
    
time.sleep(10)
#penggunaan split dibutuhkan [0] dan [1] sebagai penunjuk dimana 0 diawal dan 1 di belakang

#Zoelfan A.H
#Trisakti University
