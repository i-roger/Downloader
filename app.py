import PySimpleGUI as sg
import os
from pytube import YouTube

def window_init() :
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Video Downloader', justification= 'center', size=(600))],
        [sg.Input(key='link', justification= 'center', size=(600))],
        [sg.Button('Download .MP4', expand_x=True), sg.Button('Download .MP3', expand_x=True), sg.Button('Alterar Diretorio', expand_x=True)]
    ]

    return sg.Window('Video Downloader Desenvolvido por: Matheus Roger', layout, size=(600,300))

window = window_init()

while True:
    event, values = window.read()

    if event == 'Download .MP4': #Faz Download do video e audio (.MP4)
        url = values['link']
        yt = YouTube(str(url))
        print("Title:", yt.title)
        print("View:", yt.views)
        yd = yt.streams.get_highest_resolution()
        yd.download('D:\Downloads') # <----- Diretório! ##########################################
        sg.popup('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views)

    if event == 'Download .MP3': #Faz Download apenas do Audio (.MP3)
        url = values['link']

        if (url == '') : # VALIDAÇÃO CASO URL ESTEJA VAZIA
            error = sg.popup('É necessário digitar a URL do video!!!')
        else :
            yt = YouTube(str(url))
            
            yd = yt.streams.filter(only_audio=True).first()
            out_file = yd.download('D:\Downloads')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            sg.popup('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views)

        

    # ALTERAR LOCAL DE DOWNLOAD
    #if event == 'Alterar Diretorio':
        #destination = 'D:\Downloads' # ESSA VARIÁVEL SERÁ GLOBAL PARA PODER CONFIGURAR O DESTINO DE TODOS OS EVENTOS.


    if event == sg.WIN_CLOSED:
        window.close()
        break