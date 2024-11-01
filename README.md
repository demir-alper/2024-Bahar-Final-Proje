!ÖNEMLİ! Kodu çalıştırmadan önce aşağıdaki kısımları okuyup kontrol etmelisiniz.

Kodların kusursuz  çalışması için aşağıdaki modüllerde belirtlien kısımlardaki yerleri kodu çalıştıran kişinin belirtilen şekilde düzenlemesi gerekmektedir.

- 1 - film_oneri_modul.py modülünde 37. satırda kodu çalıştıran kişi dosya yolunu proje dosyasının bulunduğu yere göre tekrar düzenlemeli. 
- 2 - film_oneri_modul.py modülünde 131. satırda kodu çalıştıran kişi CSV çıktısının çıkacağı yeri kendi bilgisayarına göre belirtmeli. 
- 3 - film_oneri_modul.py modülünde 150 satırda kodu çalıştıran kişi dosya yolunu proje dosyasının bulunduğu yere göre tekrar düzenlemeli.
- 4 - yonetici_kontrolu.py modülündeki 43. satırda kodu çalıştıran kişi yonetici modülünün yüklenmesi için dosya yolunu proje dosyasının bulunduğu yere göre tekrar düzenlemeli.
- 5 - yonetici_modul.py modülündeki 81 satırda bulunan " edef_dizin = os.path.expanduser("~/Desktop/") " kısmı yöneticinin kaydettiği log kayıtlarının kodun çalıştığı bilgisayardaki  kullanıcılar klasöründeki "Desktop" klasörüne kaydeder. Yani bu kod bilgisayardaki  şu anki yerel kullanıcının adının olduğu klasördeki "Desktop" klasörüne otomatik olarak kaydeder. log kaydını  aldıktan sonra burayı kontrol etmek gerekli.
- 6-  github üzerindeki proje dosyalari içindeki "title.basics.tsv " dosyasi yükleme boyutunu aştığından dolayı formaliteden eklenmiştir. yani programın kullanımı sırasında github üzerinden indirilen "title.basics.tsv " dosyasindan veri okumayacaktir. dosyayi indirmek için, https://datasets.imdbws.com/title.basics.tsv.gz linkinden dosyayi indirip, unzip ettikten sonra "title.basics.tsv " dosyasini proje dosyasi içindekiyle replace yapmak gerekmektedir. 



Merhaba, MovieMate! Programına Hoş Geldiniz. Bu basit program, kullanıcının girdiği film türüne göre rastgele birkaç film önerisi sunar. Program, seçtiğiniz türlere uygun filmleri veritabanından seçer ve kullanıcıya gösterir. Bu programdaki sağlanan veriler, IMDB isimli film puanlama sitesinin verilerini kullanmaktadır.

Kullanıcıların yetkileri;


 -Film Önerisi alabilme.
 -Alınan Önerileri Kaydetme.

Yöneticilerin Yetkileri;


 -Yeni bir kullanıcı ekleyebilir.
 -Belirli bir kullanıcıyı silebilir.
 -Kayıtlı Kullanıcıların Listesini Alabiilir.
 -Kayıtlı kullanıcıların kayıt olduğu tarihi liste üzreinnden görünteleyebilir.


Modüllerin İşleyişi;

- Program ana_modul_py modulunden başlar.
- ana_modul_py üzeirnde Yönetici ve Kullanıcı için olan butonlara atanmış 2 başka modul bulunur.
- Butonlardan birisi arayuz.py, diğer ise yonetici_kontrolu.py modulunu çağırır. 
- arayuz.py modulu uzerinde veritabanından kontrol edilerek kullanici verileri doğrulanır.
- yonetici_kontrolu.py modulu uzerinde yonetici verileri de dogrulanır.
- arayuz.py üzerinden modul1.py modulu acilir. 
- modul1.py modulu, kullanıcıların yaptığı film sorgularının gerçekleştiği modüldür.
- yonetici_kontrolu.py modulu üzerinde doğrulanan veriler doğruysa, yonetici_modul.py modülü çağrılır.


-alper demir, 202307105060
