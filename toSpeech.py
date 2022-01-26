import PyPDF2
import webbrowser
import pygame
from gtts import gTTS


def start_audio(text):
    audio_file = gTTS(text=text, lang='en')
    audio_file.save('speech.mp3')
    outfile = 'speech.mp3'
    pygame.init()
    pygame.mixer.music.load(outfile)
    pygame.mixer.music.play()


def text_to_speech(file_path):
    text = ""
    file_path = file_path
    pdf_reader = PyPDF2.PdfFileReader(file_path)
    for page in range(pdf_reader.numPages):
        from_page = pdf_reader.getPage(page)
        text += from_page.extractText()

    start_audio(text)
    webbrowser.open(fr'{file_path}')


def pause_speech():
    pygame.mixer.music.pause()


def unpause_speech():
    pygame.mixer.music.unpause()


def stop_speech():
    pygame.mixer.music.stop()
