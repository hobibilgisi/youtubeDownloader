import tkinter as tk
import threading
import yt_dlp

def indir():
    # Arka planda çalışacak fonksiyonu başlat
    threading.Thread(target=video_indir, daemon=True).start()

def video_indir():
    link = link_var.get()
    cozunurluk = cozunurluk_var.get()
    format_ = format_var.get()
    # Kullanıcıya bilgi ver
    durum_label.config(text="İndiriliyor...", fg="blue")
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={cozunurluk}][ext={format_}]+bestaudio[ext=m4a]/best[height<={cozunurluk}][ext={format_}]',
            'outtmpl': r'G:\009_projects\cursor_python_projects\Python_Youtube_VideoDownloader\indirilenler\%(title)s.%(ext)s',
            'ffmpeg_location': r'C:\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        durum_label.config(text="İndirme tamamlandı!", fg="green")
    except Exception as e:
        durum_label.config(text=f"Hata: {e}", fg="red")

pencere = tk.Tk()
pencere.title("YouTube Video Downloader")
pencere.geometry("500x350")
pencere.resizable(False, False)

# Başlık
baslik = tk.Label(pencere, text="YOUTUBE VİDEO DOWNLOADER", font=("Arial", 20))
baslik.pack(pady=(20, 10))

# Video Linki Girişi
link_var = tk.StringVar()
link_giris = tk.Entry(pencere, textvariable=link_var, font=("Arial", 12), width=40)
link_giris.pack(pady=(0, 10))

def on_entry_click(event):
    if link_giris.get() == "vidyo linkini yapistir":
        link_giris.delete(0, "end")
        link_giris.config(fg="black")

def on_focusout(event):
    if link_giris.get() == "":
        link_giris.insert(0, "vidyo linkini yapistir")
        link_giris.config(fg="grey")

link_giris.insert(0, "vidyo linkini yapistir")
link_giris.config(fg="grey")
link_giris.bind("<FocusIn>", on_entry_click)
link_giris.bind("<FocusOut>", on_focusout)

# Çözünürlük için OptionMenu
cozunurlukler = ["144", "240", "360", "480", "720", "1080", "1440", "2160"]
cozunurluk_var = tk.StringVar(value=cozunurlukler[4])  # Varsayılan: 720
cozunurluk_label = tk.Label(pencere, text="Cozunurluk Secin:")
cozunurluk_label.pack()
cozunurluk_menu = tk.OptionMenu(pencere, cozunurluk_var, *cozunurlukler)
cozunurluk_menu.pack(pady=(0, 10))

# Format için OptionMenu
formatlar = ["mp4", "webm", "mkv"]
format_var = tk.StringVar(value=formatlar[0])  # Varsayılan: mp4
format_label = tk.Label(pencere, text="Format Seçin:")
format_label.pack()
format_menu = tk.OptionMenu(pencere, format_var, *formatlar)
format_menu.pack(pady=(0, 10))

# İndir Butonu
indir_buton = tk.Button(pencere, text="İndir", command=indir, font=("Arial", 14))
indir_buton.pack(pady=(10, 10))

# Durum etiketi (kullanıcıya bilgi vermek için)
durum_label = tk.Label(pencere, text="", font=("Arial", 12))
durum_label.pack(pady=(5, 0))

pencere.mainloop() 
