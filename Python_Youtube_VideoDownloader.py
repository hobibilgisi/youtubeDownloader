import yt_dlp

#link = input("Please enter the YouTube video link: ")
link = "https://www.youtube.com/watch?v=DoCPvMCNnbM&list=RDDoCPvMCNnbM&start_radio=1"

resolution = input("Çözünürlük girin (ör: 720, 1080): ")
video_format = input("Video formatı girin (ör: mp4, webm, mkv): ")
ydl_opts = {
    'format': f'bestvideo[height<={resolution}][ext={video_format}]+bestaudio[ext=m4a]/best[height<={resolution}][ext={video_format}]',
    'outtmpl': r'G:\009_projects\cursor_python_projects\indirilenler\%(title)s.%(ext)s',
    'ffmpeg_location': r'C:\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Download completed!")

#cd G:\009_projects\cursor_python_projects\Python_Youtube_VideoDownloader
#python Python_Youtube_VideoDownloader.py