from playwright.sync_api import sync_playwright
from pytube import YouTube
import os


def take_input():
    global name, name2
    name = input('Digite o nome do vídeo/música: ')
    name2 = name
    name.split()
    '+'.join(name)
    with open('history.txt', 'a') as musics:
        musics.write(name2 + '\n')


def play_music():
    take_input()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.youtube.com/results?search_query={name}")
        page.wait_for_timeout(1700)
        page.click("[class='style-scope ytd-video-renderer']")
        page.wait_for_timeout(6900)
        try:
            page.click("[class='ytp-ad-text ytp-ad-skip-button-text']")
        except:
            pass

        try:
            whereTime = page.locator("[class='ytp-time-duration']")
            time = whereTime.inner_text()
            x = time.find(":")
            minutes = int(time[0:x])
            seconds = int(time[x+1:])
            totalTime = (minutes * 60 + seconds) * 1000
            page.wait_for_timeout(totalTime)
            browser.close()
        except:
            page.wait_for_timeout(3600000)
            browser.close()


def watch_video():
    take_input()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.youtube.com/results?search_query={name}")
        page.wait_for_timeout(1700)
        page.click("[class='style-scope ytd-video-renderer']")
        page.wait_for_timeout(6900)
        try:
            page.click("[class='ytp-ad-text ytp-ad-skip-button-text']")
        except:
            pass

        try:
            whereTime = page.locator("[class='ytp-time-duration']")
            time = whereTime.inner_text()
            x = time.find(":")
            minutes = int(time[0:x])
            seconds = int(time[x+1:])
            totalTime = (minutes * 60 + seconds) * 1000
            page.wait_for_timeout(totalTime)
            browser.close()
        except:
            page.wait_for_timeout(3600000)
            browser.close()


def download_video():
    take_input()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.youtube.com/results?search_query={name}")
        page.wait_for_timeout(1700)
        page.click("[class='style-scope ytd-video-renderer']")
        link = str(page.url)
        video = YouTube(link)
        browser.close()
        video_or_audio = input(
            "Você quer baixar o vídeo ou apenas o áudio? (v/a): ")
        if video_or_audio == 'v':
            print(f'Fazendo download de {video.title}...')
            stream = video.streams.get_highest_resolution().download('videos/')
            print('O download foi feito na pasta "videos"')
        elif video_or_audio == 'a':
            print(f'Fazendo download de {video.title}...')
            stream = video.streams.get_audio_only().download('audios/')
            print('O download foi feito na pasta "audios"')


def see_history():
    with open('history.txt', 'r') as history:
        for word in history:
            print(word)


def erase_history():
    os.remove('history.txt')
    print('\nHistórico apagado\n')
    open('history.txt', 'x')


while (True):
    choice = int(input('''Escolha uma das opções abaixo: \n
1 - Escutar música
2 - Ver vídeo
3 - Fazer download de um vídeo
4 - Ver histórico
5 - Apagar histórico
6 - Sair

'''))
    if choice == 1:
        play_music()
    elif choice == 2:
        watch_video()
    elif choice == 3:
        download_video()
    elif choice == 4:
        see_history()
    elif choice == 5:
        erase_history()
    elif choice == 6:
        break
