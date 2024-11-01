
#alper demir, 202307105060


import tkinter as tk
from tkinter import messagebox, Toplevel
import mysql.connector
from PIL import Image, ImageTk
import os
from tkinter import filedialog, messagebox
import pandas as pd
import random





# - VERİTABANI BAĞLANTISI BURADA YAPILIR-
db = mysql.connector.connect(
    host="localhost",
    user="root",  # XAMPP varsayılan kullanıcı adı
    passwd="",    # XAMPP varsayılan şifre
    database="film_kayitlar"  # Veritabanı adı
    )




cursor = db.cursor()




# -IMDB VERİ SETİ BURADA DAHİL EDİLİR -
def yukle_dataset():
    # DATASETİN BULUNDUĞU KONUM, TERCİHE GÖRE DEĞİŞTİRİLEBİLİR
    filepath = 'C:/Users/alpde/Desktop/MovieMateProje/title.basics.tsv'
    return pd.read_csv(filepath, sep='\t', usecols=['primaryTitle', 'genres'])

# RASTGELE 5 TANE FİLM BULAN FONKSİYON BURADA TANIMLANDI

def eslesen_basliklar_bulma(genre):
    try:
        dataset = yukle_dataset()
        #TSV DOSYASINDAKİ TÜR İLE EŞLEŞEN  BAŞLIKLARI FİLTRELE
        eslesmis_basliklar = dataset[dataset['genres'].str.contains(f'^{genre}$', na=False, case=False)]['primaryTitle']

        #DİZİLERİN BÖLÜMLERİNİ GÖSTERMESİNİ ENGELLEMEK İÇİN "EPISODE" kelimesini içeren başlıklar filtrelendi.
        episode_olmayan_basliklar = eslesmis_basliklar[~eslesmis_basliklar.str.contains('episode', case=False)]

        # FİLTRELENEN BAŞLIKLARDAN RASTGELE 5 TANESİNİ SEÇMEK İÇİN RANDOM KULLANILDI
        rastgele_5_baslik = episode_olmayan_basliklar.tolist()

        #RETURN VE RANDOM BERABER KULLANILARAK 5 TANE FARKLI BAŞLIK ÖNERMESİ SAĞLANDI
        return random.sample(rastgele_5_baslik, min(5, len(rastgele_5_baslik)))
    

    except:
        return []  # HATA DURUMUNDA BOŞ LİSTE DÖNDÜRMEK İÇİN " [] "


# PENCERE OLUŞTURULDU
anapencere = tk.Tk()
anapencere.geometry('700x500')
anapencere.title('Ne izlesem?')
anapencere.attributes("-fullscreen", True)



# - ARKA PLAN RESMİ BURADA -
su_anki_dizin = os.getcwd()
arkaplan_foto_yol = os.path.join(su_anki_dizin, "arkaplan_foto.jpg")
os.system(f'python "{arkaplan_foto_yol}"')

arkaplan_resmi = ImageTk.PhotoImage(Image.open(arkaplan_foto_yol))
arkaplan = tk.Label(anapencere, image=arkaplan_resmi)
arkaplan.place(relwidth=1, relheight=1) 




# AÇIKLAMA ETİKETLERİ
aciklama_etiketleri = tk.Label(anapencere, text="TÜR GİRİNİZ VE 'ENTER' TUŞUNA BASINIZ:", fg="WHITE", bg="BLACK",font=("Helvetica", 15))
aciklama_etiketleri.pack(pady=20)

aciklama_etiketleri = tk.Label(anapencere, text="ENTER'a bastıktan sonra Biraz düşünmeme izin ver ;)", fg="WHITE", bg="BLACK",font=("Helvetica", 15))
aciklama_etiketleri.pack(pady=10)

# TUR GİRİŞİ KUTUSU İÇİN,, 
tur_girisi = tk.Entry(anapencere,fg="WHITE", bg="BLACK",font=("Helvetica", 15) )
tur_girisi.pack(pady=10)


#SONUCLARIN ETİKETİ
sonuc_label_kismi = tk.Label(anapencere, text="", bg='WHITE')
sonuc_label_kismi.pack(pady=10)

# TÜR GİRİLDİĞİNDE SONUÇLARI GÖSTEREN FONKSİYON
def eger_tur_girilirse(event):
    genre = tur_girisi.get()


    titles = eslesen_basliklar_bulma(genre)
    sonuc_label_kismi['text'] = '\n'.join(titles)
    sonuc_label_kismi.config(bg='WHITE', fg='darkblue', font=('Helvetica', 12, 'bold'), padx=10, pady=10)

tur_girisi.bind('<Return>', eger_tur_girilirse)


bilgi_metni = "Tavsiye almak için Tür Giriniz"
bilgi_etiketi = tk.Label(anapencere, text=bilgi_metni, font=("Helvetica", 20), fg="WHITE", bg="black")
bilgi_etiketi.pack(pady=5)


bilgi_metni = "Tür Listesine erişmek için aşağıdaki 'Türler' butonunu kullanabilirsiniz.)"
bilgi_etiketi = tk.Label(anapencere, text=bilgi_metni, font=("Helvetica", 15), fg="WHITE", bg="black")
bilgi_etiketi.pack(pady=5)


#CSV KAYDINI YAPAN FONKSİYON

def csv_kayidi_yapalim():
    try:
        # ŞU ANKİ TAVSİYELER SONUÇ BAŞLIĞINDAN ALINIR
        tavsiyeler = sonuc_label_kismi['text'].split('\n')
        if not tavsiyeler:
            messagebox.showinfo("Bilgi", "Öneri bulunamadı.")
            return

        # CSV YE BURADA KAYDEDİLİR 
        csv_cikisi = 'C:/Users/alpde/Desktop/MovieMate! Oneriler.csv'
        with open(csv_cikisi, 'w') as f:
            f.write("Önerilen Filmler\n")
            for title in tavsiyeler:
                f.write(f"{title}\n")

        messagebox.showinfo("Bilgi", f"Öneriler '{csv_cikisi}' dosyasına kaydedildi.")
    except:
        messagebox.showerror("Hata")

# ÖNERİLERİ KAYDETME BUTONU
oneriler_kayit_buton = tk.Button(anapencere, text="Tavsiyeleri Kaydet", command=csv_kayidi_yapalim,  font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='WHITE')
oneriler_kayit_buton.pack(pady=10)


# 'TÜRLERİ GÖRÜNTÜLEYEN FONKSİYON
def turlerin_listesini_acalim():
    try:
        # Dosya yolu
        filepath = 'C:/Users/alpde/OneDrive/final-projesi-deneme-jayhxi-main/turler.txt'

        # DOSYAYI VARSAYILAN METİN EDİTÖRÜNDE AÇMAK İÇİN 
        os.startfile(filepath)

    except:
        messagebox.showerror("Hata")


#TÜRLERİ GÖRÜNTÜLEMEK İÇİN BUTON
turler_butonu = tk.Button(anapencere, text="Türler", command=turlerin_listesini_acalim, font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='WHITE')
turler_butonu.pack(pady=10)



anapencere.mainloop()
