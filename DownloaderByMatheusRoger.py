from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from pytube import YouTube

window = ctk.CTk()
window.geometry('800x500')
window.title('Downloader | Desenvolvido por: Matheus Roger')
window.iconbitmap("./icons/Downloader_icon.ico")
window._set_appearance_mode('dark')
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


### FUNÇÕES ###
def baixarVideo():
    data = textInput.get()

    if (data == '') :
        popupUrlVazia()
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yd = yt.streams.get_highest_resolution()
        dirDownload = yd.download('./Videos') # <----- Diretório! ##########################################

        #downloadCompleto = str(yt.title, yt.views, dirDownload)
        
        print('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

        messagebox.showinfo("Download Completo!", message=downloadCompleto)

def baixarAudio():
    data = textInput.get()

    if (data == '') :
        popupUrlVazia()
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(140)
        dirDownload = stream.download(output_path='./Audios')
        print('Download do Audio Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

def sair(): ## Função para Fechar app...
    window.destroy()
### FUNÇÕES ###

window.mainloop()