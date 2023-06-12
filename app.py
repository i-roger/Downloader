import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from pytube import YouTube
''' Aplicativo Desenvolvido por : Matheus Roger 
Entre em contato: mroger.dev@gmail.com
LinkedIN: https://www.linkedin.com/in/matheus-roger-22555b235/
'''

window = ctk.CTk()
window._set_appearance_mode('dark')
window_width=800
window_height=500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
window.title('Downloader | Desenvolvido por: Matheus Roger')
window.iconbitmap('./icons/Downloader_icon.ico')
window.resizable(width=False, height=False)

yt = YouTube
def baixarVideo():
    data = textInput.get()
    if data == '':
        messagebox.showerror('Erro!', 'Por favor digite uma URL válida!')
        print('Por favor digite uma URL')
    else:
        container.pack_forget()
        yd = yt(data, on_progress_callback=on_progress)
        yd.streams.get_highest_resolution().download('./Videos')
        download_completo = ctk.CTkFrame(master=window, width=650, height=250)
        download_completo.pack(side='bottom', pady= 20)
        Font = ctk.CTkFont(size=20)
        infoFont = ctk.CTkFont(size=12)
        ctk.CTkLabel(download_completo, font=Font, corner_radius=10, text='DOWNLOAD COMPLETO!').place(relx=0.5, rely=0.12, anchor='center')
        ctk.CTkLabel(download_completo, font=Font, text='Titulo do arquivo:').place(relx=0.35, rely=0.35, anchor='center')
        ctk.CTkLabel(download_completo, font=infoFont, corner_radius=10, fg_color='#248A3D', text=yd.title, wraplength=140).place(relx=0.65, rely=0.35, anchor='center')
        ctk.CTkLabel(download_completo, font=Font, text='Visualizações:').place(relx=0.35, rely=0.6, anchor='center')
        ctk.CTkLabel(download_completo, font=infoFont, text=yd.views, corner_radius=10, fg_color='#248A3D').place(relx=0.65,rely=0.6, anchor='center')
    def abrirDiretorio():
        os.startfile(os.path.normpath('./Videos'))
        pPercentage.configure(window, text="0%")
        progressBar.configure(progress_color="#007AFF")
        progressBar.set(0)
    def voltar():
        pPercentage.configure(window, text="0%")
        progressBar.configure(progress_color="#007AFF")
        progressBar.set(0)
        download_completo.destroy()
        container.pack(side='bottom', pady= 60)
    ctk.CTkButton(download_completo, text="Abrir local do arquivo", height=40, command=abrirDiretorio).place(relx=0.70, rely=0.85, anchor='center')
    ctk.CTkButton(download_completo, text="Voltar", height=40, command=voltar).place(relx=0.30, rely=0.85, anchor='center')
def baixarAudio():
    data = textInput.get()
    if data == '':
        messagebox.showerror('Erro!', 'Por favor digite uma URL válida!')
        print('Por favor digite uma URL')
    else:
        container.pack_forget()
        yd = yt(data, on_progress_callback=on_progress)
        yd.streams.filter(only_audio=True)
        stream = yd.streams.get_by_itag(140)
        stream.download('./Audios')
        download_completo = ctk.CTkFrame(master=window, width=650, height=250)
        download_completo.pack(side='bottom', pady= 20)
        Font = ctk.CTkFont(size=20)
        infoFont = ctk.CTkFont(size=12)
        ctk.CTkLabel(download_completo, font=Font, corner_radius=10, text='DOWNLOAD COMPLETO!').place(relx=0.5, rely=0.12, anchor='center')
        ctk.CTkLabel(download_completo, font=Font, text='Titulo do arquivo:').place(relx=0.35, rely=0.35, anchor='center')
        ctk.CTkLabel(download_completo, font=infoFont, corner_radius=10, fg_color='#248A3D', text=yd.title, wraplength=140).place(relx=0.65, rely=0.35, anchor='center')
        ctk.CTkLabel(download_completo, font=Font, text='Visualizações:').place(relx=0.35, rely=0.6, anchor='center')
        ctk.CTkLabel(download_completo, font=infoFont, text=yd.views, corner_radius=10, fg_color='#248A3D').place(relx=0.65,rely=0.6, anchor='center')
    def abrirDiretorio():
        os.startfile(os.path.normpath('./Audios'))
        pPercentage.configure(window, text="0%")
        progressBar.configure(progress_color="#007AFF")
        progressBar.set(0)
    def voltar():
        pPercentage.configure(window, text="0%")
        progressBar.configure(progress_color="#007AFF")
        progressBar.set(0)
        download_completo.destroy()
        container.pack(side='bottom', pady= 60)
    ctk.CTkButton(download_completo, text="Abrir local do arquivo", height=40, command=abrirDiretorio).place(relx=0.70, rely=0.85, anchor='center')
    ctk.CTkButton(download_completo, text="Voltar", height=40, command=voltar).place(relx=0.30, rely=0.85, anchor='center')

def on_progress(stream, chunks, bytes_remaining) :
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentageOfCompletion = bytes_downloaded / total_size * 100
    per = str(int(percentageOfCompletion))
    pPercentage.configure(window, text = per + '%')
    pPercentage.update()
    progressBar.set(float(percentageOfCompletion) / 100)
    if per == '100' :
        progressBar.configure(progress_color="#28CD41")
img = Image.open('./icons/logonew500x250.png')
newImg = ctk.CTkImage(
dark_image=img,
size=(500,250)
)
logoTopo = ctk.CTkLabel(window, image = newImg, text="")
logoTopo.place(relx=0.5, rely=0.25, anchor='center')
pPercentage = ctk.CTkLabel(window, text="0%")
pPercentage.place(relx=0.225, rely=0.52, anchor='center')
progressBar = ctk.CTkProgressBar(window, progress_color='#007AFF',width=400)
progressBar.set(0)
progressBar.place(relx=0.5, rely=0.52, anchor='center')
container = ctk.CTkFrame(master=window, width=650, height=150)
container.pack(side='bottom', pady= 60)
text1 = ctk.CTkLabel(master=container, text="Digite sua URL:")
text1.place(relx=0.11, rely=0.15, anchor='center')
text2 = ctk.CTkLabel(master=container, text="Exemplo: (https://www.youtube.com/watch?v=xxxxxxxxxxxx)")
text2.place(relx=0.7, rely=0.15, anchor='center')
textInput = ctk.CTkEntry(master=container, width=600)
textInput.place(relx=0.5, rely=0.35, anchor='center')
btn1 = ctk.CTkButton(master=container, text="Download Video", corner_radius=10, command=baixarVideo, height=40)
btn1.place(relx=0.30, rely=0.75, anchor='center')
btn2 = ctk.CTkButton(container, text="Download Audio", corner_radius=10, command=baixarAudio, height=40)
btn2.place(relx=0.70, rely=0.75, anchor='center')

window.mainloop()