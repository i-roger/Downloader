import customtkinter as ctk
from pytube import YouTube

window = ctk.CTk()
window.geometry('800x500')
window.title('App')
window._set_appearance_mode('dark')

### FUNÇÕES ###
def baixarVideo():
    data = textInput.get()

    if (data == '') :
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yd = yt.streams.get_highest_resolution()
        dirDownload = yd.download('./Videos') # <----- Diretório! ##########################################
        print('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

def baixarAudio():
    data = textInput.get()

    if (data == '') :
        print('É necessário digitar a URL do video!!!')
    else :
        yt = YouTube(data)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(140)
        dirDownload = stream.download(output_path='./Audios')
        print('Download do Audio Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', dirDownload)

def sair():
    window.destroy()
### FUNÇÕES ###

text = ctk.CTkLabel(window, text="Digite sua URL:")
text.pack()

textInput = ctk.CTkEntry(window, width=600)
textInput.pack()

btn1 = ctk.CTkButton(window, 
                     text="Download Video", 
                     corner_radius=10,
                     command= lambda: baixarVideo()
                     )
btn1.pack(pady=20)

btn2 = ctk.CTkButton(window, 
                     text="Download Audio", 
                     corner_radius=10, 
                     command= lambda: baixarAudio()
                     )
btn2.pack(pady=20)

btn3 = ctk.CTkButton(window, 
                     text="Sair", 
                     corner_radius=10, 
                     fg_color='red', 
                     hover_color='darkred',
                     command= lambda: sair()
                     )
btn3.pack(pady=20)

window.mainloop()