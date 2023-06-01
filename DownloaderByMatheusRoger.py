import os
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from pytube import YouTube

window = ctk.CTk()
theme = window._set_appearance_mode('dark')

### CALCULO PARA CENTRALIZAR JANELA NA TELA ###
window_width=800
window_height=500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
### CALCULO PARA CENTRALIZAR JANELA NA TELA ###

window.title('Downloader | Desenvolvido por: Matheus Roger')
window.iconbitmap("./icons/Downloader_icon.ico")
window.resizable(width=False, height=False)


### LOGO
img = Image.open("./icons/logonew500x250.png")
newImg = ctk.CTkImage(
    dark_image=img,
    size=(500,250)
    )

logoTopo = ctk.CTkLabel(window, image = newImg, text="")
logoTopo.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)
### LOGO

container = ctk.CTkFrame(window, width=650, height=150)
container.place(relx=0.5, rely=0.70, anchor=ctk.CENTER)

text1 = ctk.CTkLabel(container, text="Digite sua URL:")
text1.place(relx=0.11, rely=0.15, anchor=ctk.CENTER)

text2 = ctk.CTkLabel(container, text="Exemplo: (https://www.youtube.com/watch?v=xxxxxxxxxxxx)")
text2.place(relx=0.7, rely=0.15, anchor=ctk.CENTER)

textInput = ctk.CTkEntry(container, width=600)
textInput.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

btn1 = ctk.CTkButton(container,
                     text="Download Video", 
                     corner_radius=10,
                     command= lambda: baixarVideo(),
                     height=40
                     )
btn1.place(relx=0.30, rely=0.65, anchor=ctk.CENTER)

btn2 = ctk.CTkButton(container, 
                     text="Download Audio", 
                     corner_radius=10,
                     command= lambda: baixarAudio(),
                     height=40
                     )
btn2.place(relx=0.70, rely=0.65, anchor=ctk.CENTER)

def popupUrlVazia():
    messagebox.showerror("Error !!!", "É necessário digitar a URL do video!")

# def popupDownloadCompleto():
#             popupOk = ctk.CTk()
#             popupOk_width=400
#             popupOk_height=300
#             screen_width = popupOk.winfo_screenwidth()
#             screen_height = popupOk.winfo_screenheight()
#             position_top = int(screen_height/2 - popupOk_height/2)
#             position_right = int(screen_width/2 - popupOk_width/2)
#             popupOk.geometry(f'{popupOk_width}x{popupOk_height}+{position_right}+{position_top}')

#             titleTxt = ctk.CTkLabel(popupOk, text=('Download Completo!'))
#             titleTxt.place(relx=0.2, rely=0.1, anchor=CENTER)

#             NomeArquivo = ctk.CTkLabel(popupOk, text=('Nome do Arquivo:'))
#             NomeArquivo.place(relx=0.2, rely=0.3, anchor=CENTER)

#             dataNomeArquivo = ctk.CTkLabel(popupOk, text="yt.title")
#             dataNomeArquivo.place(relx=0.4, rely=0.3, anchor=CENTER)

#             views = ctk.CTkLabel(popupOk, text=('Visualizações:'))
#             views.place(relx=0.2, rely=0.5, anchor=CENTER)

#             dataViews = ctk.CTkLabel(popupOk, text="yt.views")
#             dataViews.place(relx=0.4, rely=0.5, anchor=CENTER)

#             diretorioDestino = ctk.CTkLabel(popupOk, text=('Visualizações:'))
#             diretorioDestino.place(relx=0.2, rely=0.7, anchor=CENTER)

#             dataDestino = ctk.CTkLabel(popupOk, text="dirDownload")
#             dataDestino.place(relx=0.4, rely=0.7, anchor=CENTER)

#             popupOk.mainloop()

# popupDownloadCompleto()


### FUNÇÕES ###
def baixarVideo():
    data = textInput.get()

    if (data == '') :
        popupUrlVazia()
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yd = yt.streams.get_highest_resolution()
        dirDownload = yd.download('.\Videos') # <----- Diretório! ##########################################
        

        def popupDownloadCompleto():
            popupOk = ctk.CTk()
            popupOk_width=400
            popupOk_height=300
            screen_width = popupOk.winfo_screenwidth()
            screen_height = popupOk.winfo_screenheight()
            position_top = int(screen_height/2 - popupOk_height/2)
            position_right = int(screen_width/2 - popupOk_width/2)
            popupOk.geometry(f'{popupOk_width}x{popupOk_height}+{position_right}+{position_top}')
            popupOk.title("Download Completo!")
            popupOk.iconbitmap("./icons/Downloader_icon.ico")

            def abrirDiretorio(): # ABRE DIRETÓRIO DE VIDEO, RETIRANDO NOME DO ARQUIVO E FORMATO.
                os.startfile(dirDownload.replace(yt.title,"").replace('.mp4',""))
                popupOk.destroy()

            titleTxt = ctk.CTkLabel(popupOk, text=('Download Completo!'))
            titleTxt.place(relx=0.2, rely=0.1, anchor=CENTER)

            NomeArquivo = ctk.CTkLabel(popupOk, text=('Nome do Arquivo:'))
            NomeArquivo.place(relx=0.2, rely=0.3, anchor=CENTER)

            dataNomeArquivo = ctk.CTkLabel(popupOk, text=yt.title)
            dataNomeArquivo.place(relx=0.4, rely=0.3, anchor=CENTER)

            views = ctk.CTkLabel(popupOk, text=('Visualizações:'))
            views.place(relx=0.2, rely=0.5, anchor=CENTER)

            dataViews = ctk.CTkLabel(popupOk, text=yt.views)
            dataViews.place(relx=0.4, rely=0.5, anchor=CENTER)

            openDir = ctk.CTkButton(popupOk, text="Abrir local do arquivo", command= lambda: abrirDiretorio())
            openDir.place(relx=0.5, rely=0.7, anchor=CENTER)

            popupOk.mainloop()

        popupDownloadCompleto()


        print('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

def baixarAudio():
    data = textInput.get()

    if (data == '') :
        popupUrlVazia()
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(140)
        dirDownload = stream.download('./Audios')

        def popupDownloadCompleto():
            popupOk = ctk.CTk()
            popupOk_width=400
            popupOk_height=300
            screen_width = popupOk.winfo_screenwidth()
            screen_height = popupOk.winfo_screenheight()
            position_top = int(screen_height/2 - popupOk_height/2)
            position_right = int(screen_width/2 - popupOk_width/2)
            popupOk.geometry(f'{popupOk_width}x{popupOk_height}+{position_right}+{position_top}')
            popupOk.title("Download Completo!")
            popupOk.iconbitmap("./icons/Downloader_icon.ico")

            def abrirDiretorio(): # ABRE DIRETÓRIO DE AUDIO, RETIRANDO NOME DO ARQUIVO E FORMATO.
                os.startfile(dirDownload.replace(yt.title,"").replace('.mp4',""))
                popupOk.destroy()

            titleTxt = ctk.CTkLabel(popupOk, text=('Download Completo!'))
            titleTxt.place(relx=0.2, rely=0.1, anchor=CENTER)

            NomeArquivo = ctk.CTkLabel(popupOk, text=('Nome do Arquivo:'))
            NomeArquivo.place(relx=0.2, rely=0.3, anchor=CENTER)

            dataNomeArquivo = ctk.CTkLabel(popupOk, text=yt.title)
            dataNomeArquivo.place(relx=0.4, rely=0.3, anchor=CENTER)

            views = ctk.CTkLabel(popupOk, text=('Visualizações:'))
            views.place(relx=0.2, rely=0.5, anchor=CENTER)

            dataViews = ctk.CTkLabel(popupOk, text=yt.views)
            dataViews.place(relx=0.4, rely=0.5, anchor=CENTER)

            openDir = ctk.CTkButton(popupOk, text="Abrir local do arquivo", command= lambda: abrirDiretorio())
            openDir.place(relx=0.5, rely=0.7, anchor=CENTER)

            popupOk.mainloop()

        popupDownloadCompleto()

        print('Download do Audio Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

def sair(): ## Função para Fechar app...
    window.destroy()
### FUNÇÕES ###

window.mainloop()