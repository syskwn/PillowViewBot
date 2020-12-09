import subprocess
import webbrowser
import time


def main():
    vid_url = input("URL OF VIDEO: ")
    num_of_views = int(input("AMOUNT OF VIEWS BE CAREFUL IT MIGHT CRASH YOUR COMPUTER: "))

    def opening_web():
        webbrowser.register('firefox', None,
                            webbrowser.BackgroundBrowser("C:/Program Files/Mozilla Firefox/firefox.exe"))
        webbrowser.get('firefox').open_new_tab(vid_url)

    for i in range(num_of_views):
        opening_web()
        print(i)

    def killing_of_the_links():
        subprocess.run('TASKKILL /F /IM firefox.exe')

    kill_input = input("PRESS ENTER IF YOU WANT THE PAIN TO STOP")

    if kill_input == "":
        killing_of_the_links()
    else:
        killing_of_the_links()


main()
sid = input("WANNA RESTART? ")

if sid == 'yes':
    main()
else:
    exit()
