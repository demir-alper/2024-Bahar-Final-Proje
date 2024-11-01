
#alper demir, 202307105060


import tkinter as tk
from tkinter import messagebox, Toplevel
import mysql.connector
from PIL import Image, ImageTk
import os
import datetime

class Veritabani:
    def __init__(self):
        self.db = self.baglanti()
        self.cursor = self.db.cursor() if self.db else None

    def baglanti(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="film_kayitlar"
            )
            return db
        except mysql.connector.Error:
            messagebox.showerror("Veritabanı Hatası","Veritabanına bağlanılamadı:")

class Kullanici:
    def __init__(self, isim, tel_no, veritabani):
        self.isim = isim
        self.tel_no = tel_no
        self.veritabani = veritabani

    def giris_yap(self):
        cursor = self.veritabani.cursor
        cursor.execute('SELECT * FROM kaydedilen WHERE id=%s AND telno=%s', (self.isim, self.tel_no))
        if cursor.fetchone():
            messagebox.showinfo("Giriş Bilgisi", "Giriş başarılı!")


            
            su_anki_dizin = os.getcwd()
            film_oneri_modul_yol = os.path.join(su_anki_dizin, "film_oneri_modul.py")
            os.system(f'python "{film_oneri_modul_yol}"')
            
        
        
        
        else:
            messagebox.showinfo("Giriş Bilgisi", "Giriş başarısız! Lütfen kayıt olun.")

    def kayit_ol(self):
        cursor = self.veritabani.cursor
        try:
            cursor.execute('INSERT INTO kaydedilen (id, telno) VALUES (%s, %s)', (self.isim, self.tel_no))
            self.veritabani.db.commit()
            
            # ŞU ANKİ ZAMANI KULLANMAK İÇİN DEĞİŞKEN
            kayit_tarihi = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # ZAMAN, TELEFON, VE KULLANICI ADININ KAYDININ VERİTABANINA YAPILIŞI
            cursor.execute('INSERT INTO log_kayitlari (kullanici_id, kayit_tarihi, telno_log) VALUES (%s, %s, %s)', (self.isim, kayit_tarihi, self.tel_no))
            self.veritabani.db.commit()
            
            messagebox.showinfo("Kayıt Bilgisi", "Kayıt başarılı!")
        except mysql.connector.Error:
            messagebox.showerror("Veritabanı Hatası")


def giris_yap_gui():
    isim = isim_giris.get()
    tel_no = telno_giris.get()
    kullanici = Kullanici(isim, tel_no, veritabani)
    kullanici.giris_yap()

def kayit_penceresi():
    kayit_win = Toplevel()
    kayit_win.title("Kayıt Ekranı")
    kayit_win.geometry("300x200")
    
    tk.Label(kayit_win, text="İsim:", font=("Helvetica", 12)).pack()
    isim_girisi = tk.Entry(kayit_win, font=("Helvetica", 12))
    isim_girisi.pack()

    tk.Label(kayit_win, text="Telefon Numarası:", font=("Helvetica", 12)).pack()
    telno_girisi = tk.Entry(kayit_win, font=("Helvetica", 12))
    telno_girisi.pack()

    tk.Button(kayit_win, text="Kaydet", command=lambda: kayit_ol_gui(isim_girisi, telno_girisi)).pack()

def kayit_ol_gui(isim_girisi, telno_girisi):
    isim = isim_girisi.get()
    tel_no = telno_girisi.get()
    kullanici = Kullanici(isim, tel_no, veritabani)
    kullanici.kayit_ol()

# PROGRAMI BAŞLATMA KISMI -- 
veritabani = Veritabani()

anapencere = tk.Tk()
anapencere.title("MOVIEMATE! Giriş Ekranı")
anapencere.geometry('700x500')
anapencere.attributes("-fullscreen", True)


# - ARKA PLAN RESMİ BURADA -
su_anki_dizin = os.getcwd()
arkaplan_foto_yol = os.path.join(su_anki_dizin, "arkaplan_foto.jpg")
os.system(f'python "{arkaplan_foto_yol}"')

arkaplan_resmi = ImageTk.PhotoImage(Image.open(arkaplan_foto_yol))
arkaplan = tk.Label(anapencere, image=arkaplan_resmi)
arkaplan.place(relwidth=1, relheight=1) 

# HOŞ GELDİNİZ YAZSISI
tk.Label(anapencere, text="Hoş Geldiniz", font=("Helvetica", 24), bg="black", fg="white").pack(pady=20)

# KULLANICI İSİM GİRİŞ
isim_etiket = tk.Label(anapencere, text="İsim:", font=("Helvetica", 16), bg="black", fg="white")
isim_etiket.pack()
isim_giris = tk.Entry(anapencere, bg="black", fg="white", font=("Helvetica", 14))
isim_giris.pack(pady=5)

# KULLANICI TELEFON NUMARASI GİRİŞİ
telno_etiket = tk.Label(anapencere, text="Telefon Numarası:", font=("Helvetica", 16), bg="black", fg="white")
telno_etiket.pack()
telno_giris = tk.Entry(anapencere, bg="black", fg="white", font=("Helvetica", 14))
telno_giris.pack(pady=5)

# GİRİŞ VE KAYIT DÜĞMELERİ
giris_buton = tk.Button(anapencere, text="Giriş Yap", command=giris_yap_gui, bg="#4CAF50", fg="white", font=("Helvetica", 14))
giris_buton.pack(pady=10)
kayit_buton = tk.Button(anapencere, text="Kayıt Ol", command=kayit_penceresi, bg="#F44336", fg="white", font=("Helvetica", 14))
kayit_buton.pack(pady=10)

# Bilgi metni
bilgi_metni = "Film Tavsiyesi almak için giriş yapınız veya kayıt olunuz."
bilgi_etiketi = tk.Label(anapencere, text=bilgi_metni, font=("Helvetica", 12), fg="white", bg="black")
bilgi_etiketi.pack(pady=10)

anapencere.mainloop()
