import numpy as np
import pandas as pd

#seri oluşturma
liste1 = np.array([10,20,30,40])
liste2 = ["veri 1","veri 2","veri 3","veri 4"]
pdliste = pd.Series(data = liste1,index = liste2)

#seri toplama
pdliste + pdliste

#DataFrame oluşturma
liste1 = np.array([[10,20,30],[10,20,30],[10,20,30]])
#index 1. boyut için eleman adlari dizilimi
#columns 2. boyut için eleman adlari dizilimi
dataframe = pd.DataFrame(liste1,index=["satir 1","satir 2","satir 3"],columns=["veri 1","veri 2","veri 3"])

#DataFrame belli columns ları listeleme
dataframe["veri 1"]
dataframe[["veri 1","veri 2"]]

#DataFrame belli index leri listeleme
dataframe.loc["satir 1"]
dataframe.loc[["satir 1","satir 2"]]
#index numarası ile gitme
dataframe.iloc[0] # bir yeri alma
dataframe.iloc[[0,2]] # birden çok yeri alma
dataframe.iloc[0,2] # matris gibi ulaşma

#yeni columns ekleme
dataframe["yeni columns"] = 50

#columns silme
dataframe.drop("yeni columns",axis=1)
#row(index) silme
dataframe.drop("yeni columns",axis=0)

#dizi gibi değer ulaşma
dataframe.loc["satir 1"]["veri 2"]
dataframe.loc["satir 1","veri 2"]

#değerleri kontrol etmek
dataframe < 5 # < yerine her türlü kontrol yapılabilinir

#ÇOK ÖNEMLİ
#dataframe filtreleme
dataframe[dataframe["satir 1"] > 0]

#indexleri gösterme ve resetleme "indexleri silmez"
dataframe.reset_index()

#index değiştirme
yenidataframe = ["yeni satir 1","yeni satir 2","yeni satir 3"]
dataframe["yeni index"] = yenidataframe
#yeni değişkene atamak
degisenDataFrame = dataframe = dataframe.set_index("yeni index")
#veya aynı değişkene sabitlemek
dataframe.set_index("yeni index",inplace=True)

#multi index
ilkindexler = ["dis index 1","dis index 1","dis index 1","dis index 2","dis index 2","dis index 2"]
icindex = ["ic index 1","ic index 2","ic index 3","ic index 4","ic index 5","ic index 6"]
birlesmisindex=list(zip(ilkindexler,icindex))
birlesmisindex = pd.MultiIndex.from_tuples(birlesmisindex)
veriler = np.array([[10,"A"],[20,"C"],[50,"D"],[30,"C"],[10,"G"],[40,"A"]])
verilerDataFrame= pd.DataFrame(veriler,index=birlesmisindex,columns=["YAS","Meslek"])
verilerDataFrame

#multi index veri çağırma
verilerDataFrame.loc["dis index 1"]
#veya
verilerDataFrame.loc["dis index 2"].loc["ic index 4"]

#indexlere isim vermek
verilerDataFrame.index.names= ["bolumler","ic indexler"]

#Eksik Veriler
sozlukverisi = {"istanbul":[30,29,np.nan],"ankara":[20,np.nan,25],"izmir":[40,39,38]}
havadurumuveri = pd.DataFrame(sozlukverisi)

#boş olan veri satırını silme
havadurumuveri.dropna()

#bütün verilerin birbirleri ile olan ilişkileri
havadurumuveri.corr()

#belli veriye göre tüm ilişkiler
havadurumuveri.corr()["istanbul"].sort_values()

#boş olan veri column silmes
havadurumuveri.dropna(axis=1)

#thresh degeri girilen kadar NaN olanları silme
havadurumuveri.dropna(axis=1,thresh=2)

#boş olan yere belli sayı girmek
havadurumuveri.fillna(20)

#Gruplandırmak
maasSozluk = {"Departman" : ["Yazılım", "Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
"isimler": ["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
"Maas":[100,150,200,300,400,500]}
maasDataframe = pd.DataFrame(maasSozluk)
grupObjesi = maasDataframe.groupby("Departman")

#elemanları gösterme
grupObjesi.count()

#Grupların ortalama maaslari hesaplama
grupObjesi.mean()

#min max ozellikler
grupObjesi.max()
grupObjesi.min()

#grupların tüm özellikleri
grupObjesi.describe()

#dataframeleri birleştirmek
Sozluk1 = {"isimler": ["Ahmet","Fatma"],
"Maas":[100,500]}
Sozluk2 = {"isimler": ["Atil","Zeynep"],
"Maas":[150,400]}
Sozluk3 = {"isimler": ["Mehmet","Burak"],
"Maas":[200,300]}
Sozluk1 = pd.DataFrame(Sozluk1, index=[0,1])
Sozluk2 = pd.DataFrame(Sozluk2, index=[2,3])
Sozluk3 = pd.DataFrame(Sozluk3, index=[4,5])
#birleştirme metodu
pd.concat([Sozluk1,Sozluk2,Sozluk3])

#ortak isimleri olan sözlükleri birleştirme
mergeSozluk1 = pd.DataFrame({"isimler": ["Atil","Zeynep"],
"Maas":[100,500]})
mergeSozluk2 = pd.DataFrame({"isimler": ["Atil","Zeynep"],
"Meslek":["Muhendis","Sporcu"]})
#on yazan yere ortak kısım yazılır
pd.merge(mergeSozluk1,mergeSozluk2,on="isimler")

#dataframe de girilen bölümde kaç farklı veri olduğunu bulma
sozluk4 = {"Departman" : ["Yazılım", "Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
"isimler": ["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
"Maas":[100,150,200,300,400,500]}
sozluk4 = pd.DataFrame(sozluk4)
#isimleriyle beraber
sozluk4["Departman"].unique()
#sadece sayıyla
sozluk4["Departman"].nunique()
#detaylı
sozluk4["Departman"].value_counts()

#tüm değerler ile işlemler yapmak
def veriDegistir(veri):
    return veri * 3 + 4 - 1 / 2
sozluk4["Maas"].apply(veriDegistir)

#eksik değerleri true döndürme
sozluk4.isnull()

#tablo aynı ad bölüm birleştirme ve aynı addaki değerlerle işlemler
sozluk5 = {"Departman" : ["Yazılım", "Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
"isimler": ["Ahmet","Mehmet","Atil","Burak","Fatma","Fatma"],
"Maas":[100,150,200,300,400,500]}
sozluk5 = pd.DataFrame(sozluk5)
#standart halde iki aynı verinin ortalamasını alır
sozluk5.pivot_table(values="Maas",index=["Departman","isimler"])
#sonuna eklenen ile işlem belirlenir
sozluk5.pivot_table(values="Maas",index=["Departman","isimler"],aggfunc=np.sum())


#exel dosyası ile çalışmak
dataframe = pd.read_excel("Dosya adi.xlsx")

#veriyi exel e çevirmek
dataframe.to_excel("Dosya adi.xlsx")

#diger data dosya formatları da aynı şekilde yapılır