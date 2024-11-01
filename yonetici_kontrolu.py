
#alper demir, 202307105060

from tkinter import messagebox, Toplevel
import mysql.connector
from tkinter import filedialog, messagebox
import os
import tkinter as tk
import pandas as pd
import random
from PIL import Image, ImageTk



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="film_kayitlar"
)

cursor = db.cursor()




class Yonetici:
    def __init__(self, db_connection, cursor):
        self.db_connection = db_connection
        self.cursor = cursor

    def giris_yap(self, kullanici_adi, sifre, mail):
        # Veritabanında giriş bilgilerini kontrol et
        query = "SELECT * FROM yonetici_verileri WHERE yonetici_ismi = %s AND yonetici_sifre = %s AND yonetici_mail = %s"
        self.cursor.execute(query, (kullanici_adi, sifre, mail))
        veri = self.cursor.fetchone()

        if veri:
            # GİRİŞ BAŞARILI İSE UYARIDAN SONRA YONETCI MODUULUNU CALISTIRAN KOD 
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            
            # YONETICI MODULULU
            os.system('python "C:/Users/alpde/Desktop/MovieMateProje/yonetici_modul.py"')
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")


# YÖNETİCİ GİRİŞ BUTONU İÇİN CLASS ÜZERİNDEN CALLBACK YAPILIR 

def giris_yap_butonu_callback():
    # YÖNETİCİ VERİLERİ ALINIR
    kullanici_adi = kullanici_adi_girisi.get()
    sifre = sifre_girisi.get()
    mail = mail_girisi.get()

    # YÖNETİCİ SINIFININ BİR ÖRNEĞİ OLUŞTURULUP BİR DEĞİŞKENE ATANIR
    yonetici = Yonetici(db, cursor)
    
    # -- GİRİŞ İŞLEMİ
    yonetici.giris_yap(kullanici_adi, sifre, mail)








# TAM EKRAN ĞPENCERE OLUTŞURULDU
anapencere = tk.Tk()
anapencere.title("Yönetici Girişi")
anapencere.geometry('700x500') 
anapencere.attributes("-fullscreen", True)


# - ARKA PLAN RESMİ BURADA - 
su_anki_dizin = os.getcwd()
arkaplan_foto_yol = os.path.join(su_anki_dizin, "arkaplan_foto.jpg")
os.system(f'python "{arkaplan_foto_yol}"')

arkaplan_resmi = ImageTk.PhotoImage(Image.open(arkaplan_foto_yol))
arkaplan = tk.Label(anapencere, image=arkaplan_resmi)
arkaplan.place(relwidth=1, relheight=1) 



# KULLANICI ADI ETİKETİ VE GİRİŞ İÇİN KUTU
kullanici_adi_etiket = tk.Label(anapencere, text="Kullanıcı Adı:", bg="black", fg="white", font=("Helvetica", 14))
kullanici_adi_etiket.pack(pady=10)
kullanici_adi_girisi = tk.Entry(anapencere, bg="black", fg="white", font=("Helvetica", 14))
kullanici_adi_girisi.pack(pady=10)


# MAİL İÇİN ETİKET VE GİRİŞ KUTUSU
mail_etiket = tk.Label(anapencere, text="E-Posta Adresi:", bg="black", fg="white", font=("Helvetica", 14))
mail_etiket.pack(pady=10)
mail_girisi = tk.Entry(anapencere, bg="black", fg="white", font=("Helvetica", 14))
mail_girisi.pack(pady=10)



# ŞİFRE İÇİN ETİKET VE GİRİŞ ŞİFRE GİRİŞİ KUTUSU
sifre_etiket = tk.Label(anapencere, text="Şifre:", bg="black", fg="white", font=("Helvetica", 14))
sifre_etiket.pack(pady=10)
sifre_girisi = tk.Entry(anapencere, show="*", bg="black", fg="white", font=("Helvetica", 14))
sifre_girisi.pack(pady=10)

# GİRİŞ BUTON
giris_butonu = tk.Button(anapencere, text="Giriş Yap", command=giris_yap_butonu_callback, bg="black", fg="white", font=("Helvetica", 14))
giris_butonu.pack(pady=10)






#ANA PENCERYİ BAŞLATMA
anapencere.mainloop()
