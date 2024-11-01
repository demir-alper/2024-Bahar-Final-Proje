

#alper demir, 202307105060

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import datetime

# BUTON STİLİ
buton_stili = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "BLACK",
    "fg": "white",
    "activebackground": "#45a049",
    "bd": 2,
    "relief": "raised",
    "highlightthickness": 50
}

class Yonetici:
    def __init__(self, anapencere):
        self.anapencere = anapencere
        self.anapencere.title("Yönetim Paneli")
        self.anapencere.attributes("-fullscreen", True)

        # ARKA PLAN RESMİ BURADA
        su_anki_dizin = os.getcwd()
        arkaplan_foto_yol = os.path.join(su_anki_dizin, "arkaplan_foto.jpg")
        
        arkaplan_resmi = ImageTk.PhotoImage(Image.open(arkaplan_foto_yol))
        arkaplan = tk.Label(anapencere, image=arkaplan_resmi)
        arkaplan.image = arkaplan_resmi
        arkaplan.place(relwidth=1, relheight=1)

        # LOG KAYITLARINI LİSTELEME BUTONU
        kullanici_button = tk.Button(anapencere, text="Kayıtlı Kullanıcıların Çıktısını Al", command=self.log_kayitlari_listele, **buton_stili)
        kullanici_button.pack(pady=20)

        # KULLANICI EKLEME BUTONU
        veri_ekle_button = tk.Button(anapencere, text="Kullanıcı Ekle", command=self.veri_ekleme_penceresi, **buton_stili)
        veri_ekle_button.pack(pady=20)

        # KULLANICI SİLME BUTONU
        veri_sil_button = tk.Button(anapencere, text="Kullanıcı Sil", command=self.veri_silme_penceresi, **buton_stili)
        veri_sil_button.pack(pady=20)

    # LOG KAYITLARINI VERİTABANINDAN ALIP LİSTELEYEN FONKSİYON
    def log_kayitlari_listele(self):
        try:
            # VERİTABANINA BAĞLAN
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="film_kayitlar"
            )

            cursor = db.cursor()

            # LOG KAYITLARINI VERİTABANINDAN ÇEK
            cursor.execute("SELECT kullanici_id, kayit_tarihi, telno_log FROM log_kayitlari")
            rows = cursor.fetchall()

            # VERİTABANI BAĞLANTISINI KAPAT
            cursor.close()
            db.close()

            # GEÇİCİ BİR METİN DOSYASI OLUŞTUR VE LOG KAYITLARINI YAZ
            gecici_loglar = "log_kayitlari.txt"
            with open(gecici_loglar, "w", encoding="utf-8") as dosya:
                for row in rows:
                    dosya.write(f"Kullanıcı adı: {row[0]}\n")
                    dosya.write(f"Kayıt Tarihi: {row[1]}\n")
                    dosya.write(f"Telefon Numarası: {row[2]}\n")
                    dosya.write("-------------------\n")

            # HEDEF DİZİNİ DOĞRULA
            hedef_dizin = os.path.expanduser("~/Desktop/")
            if not os.path.exists(hedef_dizin):
                os.makedirs(hedef_dizin)

            # DOSYAYI HEDEF DİZİNE TAŞI
            hedef_dosya = os.path.join(hedef_dizin, "log_kayitlari.txt")
            os.replace(gecici_loglar, hedef_dosya)

            # BAŞARI MESAJI GÖSTER
            messagebox.showinfo("Log Kayıt Bilgisi", f"Veriler başarıyla {hedef_dosya} dizinine kaydedildi!")
        except mysql.connector.Error as err:
            messagebox.showerror("Veritabanı Hatası", f"Veritabanı hatası: {err}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

    # KAYIT EKLEME PENCERESİ
    def veri_ekleme_penceresi(self):
        def kayit_ol():
            kullanici_ad = kullanici_adi_girisi.get()
            telno_degeri = telno_girisi.get()
            
            if kullanici_ad and telno_degeri:
                try:
                    db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="film_kayitlar"
                    )

                    cursor = db.cursor()
                    
                    # ANA TABLOYA EKLE
                    cursor.execute("INSERT INTO kaydedilen (id, telno) VALUES (%s, %s)", (kullanici_ad, telno_degeri))
                    
                    # MEVCUT ZAMANI KAYIT TARİHİ OLARAK AL
                    kayit_tarihi = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    # LOG KAYDINDA VERİTABANINA EKLE
                    cursor.execute("INSERT INTO log_kayitlari (kullanici_id, kayit_tarihi, telno_log) VALUES (%s, %s, %s)", (kullanici_ad, kayit_tarihi, telno_degeri))

                    db.commit()

                    cursor.close()
                    db.close()

                    messagebox.showinfo("Kayıt Bilgisi", "Kayıt başarılı!")
                    ekleme_penceresi.destroy()
                except mysql.connector.Error as err:
                    messagebox.showerror("Veritabanı Hatası", f"Veritabanı hatası: {err}")
                except Exception as e:
                    messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            else:
                messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun!")

        ekleme_penceresi = tk.Toplevel(self.anapencere)
        ekleme_penceresi.title("Kullanıcı Ekle")
        ekleme_penceresi.geometry("300x200")

        id_label = tk.Label(ekleme_penceresi, text="Eklenecek Kullanıcının Adı:")
        id_label.pack(pady=5)
        kullanici_adi_girisi = tk.Entry(ekleme_penceresi)
        kullanici_adi_girisi.pack(pady=5)

        telno_label = tk.Label(ekleme_penceresi, text="Eklenecek Kullanıcının Telefon Numarası:")
        telno_label.pack(pady=5)
        telno_girisi = tk.Entry(ekleme_penceresi)
        telno_girisi.pack(pady=5)

        ekle_button = tk.Button(ekleme_penceresi, text="Ekle", command=kayit_ol, **buton_stili)
        ekle_button.pack(pady=20)

    # KAYIT SİLME PENCERESİ
    def veri_silme_penceresi(self):
        def kayit_sil():
            kullanici_ad = kullanici_adi_girisi.get()

            if kullanici_ad:
                try:
                    db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="film_kayitlar"
                    )

                    cursor = db.cursor()
                    # HER İKİ TABLODAN VERİYİ SİL

                    cursor.execute("DELETE FROM kaydedilen WHERE id = %s", (kullanici_ad,))
                    cursor.execute("DELETE FROM log_kayitlari WHERE kullanici_id = %s", (kullanici_ad,))

                    db.commit()

                    cursor.close()
                    db.close()

                    messagebox.showinfo("Silme Bilgisi", "Silme işlemi başarılı!")
                    silme_penceresi.destroy()
                except mysql.connector.Error as err:
                    messagebox.showerror("Veritabanı Hatası", f"Veritabanı hatası: {err}")
                except Exception as e:
                    messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            else:
                messagebox.showwarning("Eksik Bilgi", "Lütfen Kullanıcı adı alanını doldurun!")

        silme_penceresi = tk.Toplevel(self.anapencere)
        silme_penceresi.title("Kullanıcı Sil")
        silme_penceresi.geometry("300x200")

        id_label = tk.Label(silme_penceresi, text="Silinecek Kullanıcının Kullanıcı adı:")
        id_label.pack(pady=5)
        kullanici_adi_girisi = tk.Entry(silme_penceresi)
        kullanici_adi_girisi.pack(pady=5)

        sil_button = tk.Button(silme_penceresi, text="Sil", command=kayit_sil, **buton_stili)
        sil_button.pack(pady=20)


# ANA PENCERE VE  UYGULAMAYI  OLUŞTUR - - 
if __name__ == "__main__":
    anapencere = tk.Tk()
    yonetici = Yonetici(anapencere)
    anapencere.mainloop()
