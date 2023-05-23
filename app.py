import PySimpleGUI as sg
from pytube import YouTube

def window_init() :
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Video Downloader', justification= 'center', size=(600))],
        [sg.Input(key='link', justification= 'center', size=(600))],
        [sg.Button('Download', expand_x=True), sg.Button('Alterar Diretorio', expand_x=True)]
    ]

    return sg.Window('Video Downloader Desenvolvido por: Matheus Roger', layout, size=(600,300))

window = window_init()

while True:
    event, values = window.read()

    if event == 'Download':
        url = values['link']
        yt = YouTube(str(url))
        print("Title:", yt.title)
        print("View:", yt.views)
        yd = yt.streams.get_highest_resolution()
        yd.download('D:\Downloads') # <----- Diretório! ##########################################
        sg.popup('Download Completo!', 'Nome do Arquivo:', yt.title)

    # ALTERAR LOCAL DE DOWNLOAD
    #if event == 'Alterar Diretorio':


    if event == sg.WIN_CLOSED:
        window.close()
        break