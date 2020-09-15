import numpy as np

#numpy dizisine çevirme
liste1 = np.array([2,3,4])

#2 sayi arasi dizi oluşturma
liste2 = np.arange(0,10)
#artarak
liste2 = np.arange(0,10,2)

#sifir dizisi
liste3 = np.zeros((3,3))

#bir dizisi
liste4 = np.ones((3,3))

#iki sayi arasinda girilen sayi kadar eşit aralıklı sayi oluşturma
liste5 = np.linspace(0,20,5)

#birim matris
liste6 = np.eye(10)

#rastgele tam sayilar
liste7 = np.random.randint(0,10,(5,5))

#dizi boyutunu yenileme
liste8 = np.array([0,1,2,3,4,5,6,7,8,9])
liste8 = liste8.reshape(2,5)

#dizi en yüksek en düşük sayi
liste8.max()
liste8.min()
#indexleri
liste8.argmax()
liste8.argmin()

#dizinin boyut bilgisi
liste8.shape

#dizi belli yerdeki elemanı değiştirme
liste9 = np.array([0,1,2,3,4,5,6])
liste9[2:5] = 5

#matris belli elemanlara ulaşma
x = 0 #x den itibaren 1. boyut
y = 2 #y ninci eleman
liste8[x:,y]# sonuna : eklenirse y ninci elemandan itibaren sonrasını alır

#belli 2. boytulara ulaşma
liste10 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]])
liste10[[2,3]] #2. boyutta 2. ve 3. dizideki elemanlar

#dizinin elemanları belli sayıdan büyük mü olduğunu kontrol edip
#sonucu ile dizi oluşturma
kontroldizisi = liste10 > 10

#dizinin elemanlarını kontrol dizisindeki true değerine göre yeni liste oluşturma
liste10[kontroldizisi]

#numpy diziler matematiksel işlemler yapabilir
liste10 - liste10
liste10 * liste10
liste10 + liste10
liste10 / liste10
np.sqrt(liste10) #kare kök
