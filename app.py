from pytube import YouTube
import PySimpleGUI as sg

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
    #CODIGO FUNCIONANDO PORÉM FUNCIONA E DEPOIS PARA DE FUNCIONAR
    if event == 'Download .MP4': #Trigger do botão DOWNLOAD MP4
        videolink = str(values['link'])
        if (videolink == '') :
            sg.popup('É necessário digitar a URL do video!!!', title='ERRO!')
        else :
            yt = YouTube(videolink)
            yd = yt.streams.get_highest_resolution()
            destinoDownload = yd.download('D:/Downloads') # <----- Diretório! ##########################################
            sg.popup('Download Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', destinoDownload)
            #print('Diretório do Download ========> ', destinoDownload)

    if event == 'Download .MP3':
        videolink = str(values['link'])
        if (videolink == ''):
            sg.popup('É necessário digitar a URL do video!!!', title='ERRO!')
        else:
            ### METODO DE DOWNLOAD BASEADO NA DOM DO PYTUBE (AUDIO)
            yt = YouTube(videolink)
            yt.streams.filter(only_audio=True)
            stream = yt.streams.get_by_itag(140)
            destinoDownload = stream.download(output_path='D:/Downloads')
            sg.popup('Download do Audio Completo!', 'Nome do Arquivo:', yt.title, 'Visualizações:', yt.views, 'Arquivo em:', destinoDownload)
            #print('Diretório do Download ========> ', destinoDownload)

    if event == sg.WIN_CLOSED:
        window.close()
        break