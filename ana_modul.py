
#alper demir, 202307105060

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ARAYÜZ VE YÖNETİCİ MODÜLLERİNİ ÇAĞIRMAK İÇİN 2 TANE FONKSİYON;

def arayuz_giris():
    su_anki_dizin = os.getcwd()
    arayuz_yol = os.path.join(su_anki_dizin, "arayuz.py")
    os.system(f'python "{arayuz_yol}"')
    

def yonetici_girisi():
    su_anki_dizin = os.getcwd()
    yonetici_kontrol_yol = os.path.join(su_anki_dizin, "yonetici_kontrolu.py")
    os.system(f'python "{yonetici_kontrol_yol}"')
   

# ANA PENCERE
anapencere = tk.Tk()
anapencere.title("MOVIEMATE! Tanıtım")
anapencere.attributes("-fullscreen", True)


# - ARKA PLAN RESMİ BURADA - 

su_anki_dizin = os.getcwd()
arkaplan_foto_yol = os.path.join(su_anki_dizin, "arkaplan_foto.jpg")
os.system(f'python "{arkaplan_foto_yol}"')

arkaplan_resmi = ImageTk.PhotoImage(Image.open(arkaplan_foto_yol))
arkaplan = tk.Label(anapencere, image=arkaplan_resmi)
arkaplan.place(relwidth=1, relheight=1) 


# BANNER! 

su_anki_dizin = os.getcwd()
banner_foto_yol = os.path.join(su_anki_dizin, "banner.png")
os.system(f'python "{banner_foto_yol}"')

banner_resmi = ImageTk.PhotoImage(Image.open(banner_foto_yol))

banner = tk.PhotoImage(file=banner_foto_yol)

banner_etiket = tk.Label(anapencere, image=banner)
banner_etiket.pack(pady=20)


# BUTON STİLLERİ İÇİN ANA DEĞİŞKEN
buton_stili = {
    "font": ("Helvetica", 15, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "bd": 2,
    "relief": "raised",
   
}

# KULLANICI GİRİŞİ BUTONU
kullanici_button = tk.Button(anapencere, text="KULLANICI GİRİŞ", command=arayuz_giris, **buton_stili)
kullanici_button.config(bg='#4CAF50')
kullanici_button.pack(pady=40)

# YÖNETİCİ GİRİŞİ BUTONU
yonetici_button = tk.Button(anapencere, text="YÖNETİCİ GİRİŞ", command=yonetici_girisi, **buton_stili)
yonetici_button.config(bg='#F44336', activebackground="#e53935")
yonetici_button.pack(pady=5)

# BİLGİ ETİKETLERİ SİYAH ÇERÇEVESİ
bilgi_cercevesi = tk.Frame(anapencere, bg='black', bd=20)
bilgi_cercevesi.pack(pady=10, fill="none", expand=True)

# BİLGİ ETİKETLERİ DİZİSİ
bilgi_metni_listesi = [
    "Merhaba, MovieMate! Programına Hoş Geldiniz",
    "Bu basit program, kullanıcının girdiği film türüne göre rastgele birkaç film önerisi sunar.",
    "Program, seçtiğiniz türlere uygun filmleri veritabanından seçer ve kullanıcıya gösterir.",
    "Bu programdaki sağlanan veriler IMDB isimli film puanlama sitesinin verilerini kullanmaktadır.",
    "Datasetlerin kaynağına aşağıdaki linkten ulaşabilirsiniz.",
    "https://developer.imdb.com/non-commercial-datasets/.",
    "ALPER DEMİR, 202307105060 ",
]

for metin in bilgi_metni_listesi:
    bilgi_etiketi = tk.Label(bilgi_cercevesi, text=metin, font=("Helvetica", 12), fg="white", bg="black", wraplength=650, justify="left")
    bilgi_etiketi.pack(pady=10)

# ANA PENCERE BAŞLANGICI

anapencere.mainloop()
