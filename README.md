# LDR ile Otomatik LED Yakma Projesi
Bu proje, bir Işığa Bağımlı Direnç (LDR) sensörünü kullanarak ortam ışığı seviyesini algılar ve bu seviyeye göre bir LED'i otomatik olarak açıp kapatır. Proje, Arduino ve Python arasında seri haberleşmeyi kullanarak yapılmıştır.
##Proje Açıklaması
Uygulamanın temel amacı, karanlık olduğunda LED'i yakmak ve ortam aydınlandığında söndürmektir. Bu otomasyon, bir PySerial modülü kullanan Python programı ve LDR sensörünü okuyan bir Arduino kartı ile gerçekleştirilir.
Arduino: LDR'den okunan analog değeri sürekli olarak seri porta gönderir.
Python: Arduino'dan gelen değerleri okur, önceden belirlenen bir eşik değerine göre ortamın karanlık veya aydınlık olduğuna karar verir ve bu duruma göre LED'i kontrol etmek için Arduino'ya komutlar ('1' veya '0') gönderir.

## Özellikler
Otomatik Kontrol: LDR sensörü aracılığıyla ortam ışığına duyarlı otomatik LED kontrolü.
Seri Haberleşme: Arduino ve Python arasında güvenilir seri iletişim.
Esnek Eşik Değeri: Python kodundaki LDR_esik_degeri değişkeni sayesinde hassasiyet kolayca ayarlanabilir.
Enerji Verimliliği: led_kontrol fonksiyonu, LED'in durumunu sadece gerektiğinde değiştirerek gereksiz komut döngüsünü önler.

## Kullanılan Teknolojiler
Donanım: Arduino Uno, LDR (Işığa Bağımlı Direnç), LED, 10k Ohm Direnç ve 220 Ohm Direnç ve Jumper kablolar.
Yazılım: Arduino IDE, Python 3.x.
Python Kütüphaneleri: pyserial, time.

# Kurulum ve Kullanım

## Yapım Aşaması
Devreyi Kurun: Board üzerine belirtilen devre elemanlarını şemaya uygun bir şekilde yerleştirin ve bağlantıları yapın.
Gerekli Kütüphaneleri Kurun: Python için pyserial kütüphanesini terminal üzerinden pip install pyserial komutu ile yükleyin.
Kodları Hazırlayın: Proje için gerekli olan hem Arduino hem de Python kodlarını yazın.

## Uygulama Aşaması
Donanımı Hazırlayın: Devreyi kurduktan sonra Arduino kartınızı USB kablosu ile bilgisayara bağlayın.
Arduino Kodunu Yükleyin: Arduino IDE'sinden kodu derleyin ve kartınıza yükleyin. Yükleme tamamlandıktan sonra Arduino IDE'sini kapatın.
Python Kodunu Çalıştırın: COM port numarasını kendi kartınıza uygun şekilde ayarladıktan sonra, Python dosyasını çalıştırın.

## Devre Şeması
![LDR Devre Şeması](images/ldr_devresemasi.png)

