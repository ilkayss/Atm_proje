print(""""
*************************
ATM PROJESINE HOSGELDINIZ
*************************

Islemler:
1-Para Yatir
2-Para Cek
3-Bakiye Sorgula

Lutfen cikmak icin * tusuna basiniz
""")

bakiye=1000

while True:
    islem = input("Lutfen yapmak istediginiz islemi seciniz : ")
    if(islem == '1'):
        miktar=int(input("Lutfen kac tl yatirmak istediginizi belirtiniz : "))
        bakiye+=miktar
    elif(islem == '2'):
        miktar=int(input("Lutfen cekmek istediginiz tutari giriniz : 1"))
        bakiye-=miktar
    elif(islem == '3'):
        print("Bakiyeniz {} TL dir".format(bakiye))
    else:
        print("gecersiz islem!!!")

    if(islem == '*'):
        print("IYI GUNLER DILERIZ")
        break