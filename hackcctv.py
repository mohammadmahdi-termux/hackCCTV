import os
import time
import sys

def loading_animation():
    symbols = ("⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿")
    for _ in range(3):
        for symbol in symbols:
            time.sleep(0.1)
            print(f"{green} ~>> Loading {symbol}", end='\r')
def loading_animation2():
    symbols = ("〡", "〢", "〣")
    for _ in range(3):
        for symbol in symbols:
            time.sleep(0.1)
            print(f"{yellow} ~>> Loading {symbol}", end='\r')



def clear_terminal():
    try:
        os.system('printf "\033c"')
    except Exception as e:
        print(f"An error occurred: {e}")

#clear_terminal
clear_terminal()






green  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
yellow ="\x1b[1;93m"
magenta   ="\x1b[1;95m"
white  ="\x1b[1;97m"
blue   ="\x1b[1;94m"
red  ='\x1b[1;91m'
underline = '\033[4m'
pink = '\033[35m'
bold = '\033[1m'
black='\033[30m'

clear_terminal()

      
while True:
    import time
    def type_text(textss):
        for char in textss:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0001)  # تنظیم کنید که سرعت تایپ را تغییر دهد
        print()
    textss = (f"""{white+bold}
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⡟⠩⣿⣿⣿⣿⣿⡟⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠡⣤⣀⠀⠻⣿⣿⣿⡟⢀⠀⡇⡆⠘⣿⣿⣿⣿⠀⣴⠘⣿⣿⣿⣿⡟⣻⣿⢻⣿⣿⣿⠟⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠈⣿⣿⣿⣿⣷⡀⢿⣿⣷⢀⣿⣿⣿⡿⢸⣧⢸⣗⡀⢿⣿⣿⡏⣴⣶⣦⢻⣿⣿⡟⢀⣿⠃⣼⣿⣿⠏⢰⣷⡄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣌⠛⢿⣿⣿⣷⢸⣿⢇⣼⣿⣿⣿⣧⣿⣿⣿⣿⡇⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⡇⣴⣶⢰⣿⣿⡿⣠⣿⣿⠅⢀⣿⣿⣿⣿⣭⢉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠻⢿⣿⣿⣿⣿⡄⣫⣴⣮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣛⣩⣴⣿⣿⣿⣿⠟⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢣⠐⡀⠙⢿⣿⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⣿⣿⣿⣿⣿⣏⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⣦⡀⣿⣶⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣬⣿⣿⣿⣿⣿⣿⠋⢀⣴⣶⣮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡿⣿⣿⣿⣿⣷⣸⣿⣾⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⢄⢠⡈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢤⣁⢻⣷⣦⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠠⣶⣄⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡐⢿⣿⣾⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣯⠈⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢼⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠣⡄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣃⠀⠿⠇⢸⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣦⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡿⣧⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣾⢿⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡟⢁⣼⣷⣾⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢿⣶⣷⣮⠻⣿⣿⣿⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠉⠉⠛⠿⢿⣿⣿⡿⢫⣴⣵⣷⡕⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⢷⣦⡌⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢻⡽⣿⣿⢤⠉⠁⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠈⠫⢾⣿⣿⢯⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠙⠛⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣦⡈⠉⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢾⣽⣿⠗⠁⠀⠀⠀⠀⠀⠀⠀⣰⣿⣄⠀⠀⠀⠀⠀⠀⠀⠐⢿⣿⣯⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠒⠛⠻⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠊⠂⠁⠀⠀⠀⠀⢀⣀⣤⣴⣿⣿⣿⣿⣷⣦⣤⣠⠀⠀⠀⠀⠀⠀⠈⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⢁⣤⣿⣿⣿⣿
             ⣿⣿⣿⢋⠉⠉⢉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣴⣶⣾⣿⣿⣿⣿⣿⣿
             ⣿⣿⣮⡛⠿⠿⠿⢷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣇⢿⣿⣿⣿⣿⣿⠜⣺⣿⣿⣷⣤⣀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠻⢿⣿
             ⣿⣿⣿⣿⣶⣦⣴⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣶⡙⣿⣿⡿⢡⣾⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣀⣴⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠇⠀⠀⠀⠀⣼⡏⣿⣿⣿⣿⣿⣿⠇⣿⣿⡇⢾⣿⣿⣿⣿⣿⣿⢿⡇⠀⠀⠀⠀⡟⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣉⠉⣉⣉⣽⣿
             ⣿⡉⠠⢤⣀⣀⣄⣭⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⠸⣮⡀⠀⢀⡴⣫⣾⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⢾⣿⣿⣿⣿⣿⣿⣶⡙⣆⡀⠀⢀⣾⢣⡎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⠉⠁⣁⣈⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡶⣜⢿⡞⣿⣧⠻⣿⣿⣿⣿⣿⡿⢟⢵⣿⣿⣿⡞⡻⣿⣿⣿⣿⣿⣿⢏⣿⣿⣱⡟⣵⢸⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⠟⠛
             ⣿⣷⣦⣤⣍⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣷⢝⢾⣷⡏⠟⣵⢦⣭⣭⠉⢷⣮⣹⡘⠿⣿⠟⣡⢿⣷⠎⠉⣭⣽⣰⣎⠟⣷⣿⡟⢡⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡌⠁⠀⠐⢾
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣇⠇⣿⣿⣆⠋⢾⣿⡀⠀⢠⡿⠃⣬⢻⣿⢟⣅⠏⣿⡀⠀⣠⣿⡇⢟⣼⣿⣳⠕⣼⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣫⣴⣿⣿⣶⣦
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⠇⣿⣾⣿⣿⣮⣽⣛⣻⣛⣁⣺⢿⣿⣿⣼⢿⣂⣈⣛⣛⣛⣭⣶⣿⣻⣷⣧⢻⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⢿⡄⢻⣟⣿⣿⣿⣿⡿⣿⣿⠿⢿⣷⢹⣿⣏⣾⡿⠿⣿⣿⣿⣿⣿⣻⣿⢿⡏⣸⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣦⣍⠻⣿⣿⣻⣧⢿⠁⣾⣶⣿⣼⣿⣧⣷⣶⡗⢸⣟⣿⣧⣿⡿⢟⣩⣾⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇⣿⢛⠀⠬⣳⠟⣟⣴⣌⣛⠿⣿⣿⣿⢟⣛⣥⣏⡺⢻⣛⠕⠠⡹⣷⢿⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⠇⣇⢏⣇⡃⡌⡻⠿⠿⢿⣻⣟⣪⢭⣕⣿⡛⡿⠿⠿⣋⢱⢘⡴⡇⡟⠸⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣝⠸⣮⠸⣟⡆⣿⡏⣿⡟⣴⡖⣭⢭⣅⢶⣎⢿⣿⢻⡿⣰⡿⢗⣼⢡⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡕⡱⣜⠵⡹⢡⣶⣾⣶⣷⠮⠶⠷⣶⣶⣶⣶⡜⠇⡷⣣⢋⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢜⣃⠰⢿⣿⣿⢟⣥⣿⣿⣷⣌⠻⣿⣿⠿⠦⡼⡑⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠜⣇⡕⣮⡱⢟⡛⣿⣙⣟⢛⡻⢂⣴⠣⡼⡱⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣾⢰⠸⢟⣨⡷⢶⢶⡶⢯⣅⡿⠇⡏⡷⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⢙⠾⠿⣋⡼⢟⣾⠻⢶⣝⠿⠷⡪⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡻⠟⢋⣴⣿⣿⣿⣦⡙⠻⣏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣽⠛⠒⠛⣯⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿


        {cyan}██╗  ██╗ █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗████████╗██╗   ██╗ {red}BETA{yellow}2{cyan}
        ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝╚══██╔══╝██║   ██║
        ███████║███████║██║     █████╔╝ ██║     ██║        ██║   ██║   ██║
        ██╔══██║██╔══██║██║     ██╔═██╗ ██║     ██║        ██║   ╚██╗ ██╔╝
        ██║  ██║██║  ██║╚██████╗██║  ██╗╚██████╗╚██████╗   ██║    ╚████╔╝ 
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝   ╚═╝     ╚═══╝  


    {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

    {green}[<ID~>github] ▪︎  {white}https://github.com/mohammadmahdi-termux
    {cyan}[<ID~>telegram] ▪︎  {white}@Mohammadmahdi_termux
    {magenta}[<ID~>instagram] ▪︎  {white}@Mohammadmahditermux\~/@Mohammadmahdi_termux

    {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺


        {yellow}╓                      {yellow}     ╖
        {yellow}╟1-{red}Hacking by {green}Time zone{yellow}     ║
        {yellow}║                      {yellow}     ║
        {yellow}╟2-{red}Hacking by {green}Location {yellow}     ║
        {yellow}║                      {yellow}     ║
        {yellow}╟3-{red}Hacking by {green}Counties {yellow}     ║
        {yellow}║                      {yellow}     ║
        {yellow}╟4-{red}Hacking by {green}Manufacturers {yellow}║
        {yellow}╙                      {yellow}     ╜""")



    lolo=("""""")       
    type_text(textss)
    

    user_input = input(f"""{green}$/> {red}Enter a number :{pink} """)
    
    if user_input.isdigit():
        choice = int(user_input)

        if choice == 1:
            clear_terminal()
            import requests
            import re
            import colorama
            import os
            import time
            import sys

            colorama.init()

            green = "\x1b[1;92m"
            cyan = "\x1b[1;96m"
            yellow = "\x1b[1;93m"
            magenta = "\x1b[1;95m"
            white = "\x1b[1;97m"
            blue = "\x1b[1;94m"
            red = '\x1b[1;91m'
            underline = '\033[4m'
            pink = '\033[35m'
            bold = '\033[1m'
            black = '\033[30m'
            def type_text(text):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.001)
                print()                 
            text = (f"""{green}
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
                ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
                ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
                ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            {yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {green}[<ID~>github] ▪︎  {white}https://github.com/mohammadmahdi-termux
            {cyan}[<ID~>telegram] ▪︎  {white}@Mohammadmahdi_termux
            {magenta}[<ID~>instagram] ▪︎  {white}@Mohammadmahditermux

            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {red}01–{green} +00:00     {red}02–{green} +01:00     {red}03–{green} +02:00     {red}04–{green} +03:00
            {red}05–{green} +03:30     {red}06–{green} +04:00     {red}07–{green} +05:00     {red}08–{green} +05:30
            {red}09–{green} +06:00     {red}10–{green} +07:00     {red}11–{green} +08:00     {red}12–{green} +09:00
            {red}13–{green} +10:00     {red}14–{green} +11:00     {red}15–{green} +13:00     {red}16–{green} -
            {red}17–{green} -02:00     {red}18–{green} -03:00     {red}19–{green} -04:00     {red}20–{green} -05:00
            {red}21–{green} -06:00     {red}22–{green} -07:00     {red}23–{green} -08:00     {red}24–{green} -09:00
            {red}25–{green} -10:00

            {red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺""")
            



            try :

                type_text(text)

                times = ["+00:00","+01:00","+02:00","+03:00","+03:30","+04:00","+05:00","+05:30","+06:00","+07:00","+07:00" ,"+08:00","+09:00","+10:00","+11:00","+13:00","-","-02:00","-03:00","-04:00","-05:00","-06:00","-07:00","-08:00","-09:00","-10:00"]

                headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36"}
                num = int(input(f"{yellow}[?]~>{red}Enter code timezone : "))
                if num not in range(1, 26):
                    raise IndexError
                text=""
                time = times[num-1]
                res = requests.get( f"http://www.insecam.org/en/bytimezone/{time}",headers=headers )
                last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get( f"http://www.insecam.org/en/bytimezone/{time}/?page={page}", headers=headers )
                    find_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", res.text)
                    print(f"""\n{bold+yellow}@Mohammadmahdi_termux""")
                    print(green+"")

                    for ip in find_ip:
                        print(ip)


            except:

                        print(red+" !ERORR❌ ")




        elif choice == 2:
            clear_terminal()
            import os
            import re
            import requests
            import time
            import sys

            green  ="\x1b[1;92m"
            cyan   ="\x1b[1;96m"
            yellow ="\x1b[1;93m"
            magenta   ="\x1b[1;95m"
            white  ="\x1b[1;97m"
            blue   ="\x1b[1;94m"
            red  ='\x1b[1;91m'
            underline = '\033[4m'
            pink = '\033[35m'
            bold = '\033[1m'
            black='\033[30m'


            def type_text(text):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.001)  # تنظیم کنید که سرعت تایپ را تغییر دهد
                print()                 
            text = (f"""{green}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
            ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
            ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
            ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            {yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {green}[<ID~>github] ▪︎  {white}https://github.com/mohammadmahdi-termux
            {cyan}[<ID~>telegram] ▪︎  {white}@Mohammadmahdi_termux
            {magenta}[<ID~>instagram] ▪︎  {white}@Mohammadmahditermux

            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

                    {yellow}01–{red}server      {yellow}02–{red}farm      {yellow}03–{red}restaurant    
                    {yellow}04–{red}park        {yellow}05–{red}brid      {yellow}06–{red}beach    
                    {yellow}07–{red}bridge      {yellow}08–{red}sport     {yellow}09–{red}shop       
                    {yellow}10–{red}airline     {yellow}11–{red}hotel     {yellow}12–{red}Bar 
                    {yellow}13–{red}House       {yellow}14–{red}Parking   {yellow}15–{red}Landscape  
                    {yellow}18–{red}Traffic     {yellow}17–{red}Nature    {yellow}19–{red}Printer
                    {yellow}19–{red}Religion    {yellow}20–{red}Laundry   {yellow}21–{red}Mountain    
                    {yellow}22–{red}x           {yellow}23–{red}Ptz       {yellow}24–{red}Energy

            {red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            """)





            try :
                type_text(text)


                locs = ["Server","Farm","Restaurant","park","bird","beach","bridge","sport","shop","Airliner","hotel","Bar","House","Parking","Landscape","Traffic","Nature","Printer","Religion","Laundry","Mountain","Architecture","Ptz","Energy"]


                headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36"}
                num = int(input(f"{yellow}[?]~>{red}Enter code location : "))
                if num not in range(1, 24+1):
                    raise IndexError

                text= ""    
                loc = locs[num-1]
                res = requests.get( f"http://www.insecam.org/en/bytag/{loc}",headers=headers )
                last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get( f"http://www.insecam.org/en/bytag/{loc}/?page={page}", headers=headers )
                    find_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", res.text)
                    print(f"""\n{bold+yellow}@Mohammadmahdi_termux""")
                    print(green+"")

                    for ip in find_ip:
                        print(ip)

            except:

                        print(red+" !ERORR❌ *call me*")


        elif choice == 3:
            clear_terminal()
            import requests
            import re
            import colorama
            colorama.init()
            import os
            import time
            import sys


            green  ="\x1b[1;92m"
            cyan   ="\x1b[1;96m"
            yellow ="\x1b[1;93m"
            magenta   ="\x1b[1;95m"
            white  ="\x1b[1;97m"
            blue   ="\x1b[1;94m"
            red  ='\x1b[1;91m'
            underline = '\033[4m'
            pink = '\033[35m'
            bold = '\033[1m'
            black='\033[30m'



            print(f"""{green}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
            ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
            ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
            ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            print(f"  {yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C")

            def type_text(text):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.001) 
                print()



            while True:
                text1=(f"""
            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {green}[<ID~>github] ▪︎  {white}https://github.com/mohammadmahdi-termux
            {cyan}[<ID~>telegram] ▪︎  {white}@Mohammadmahdi_termux
            {magenta}[<ID~>instagram] ▪︎  {white}@Mohammadmahditermux

            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {red}01–{yellow}•Albania•            {red}02–{yellow}•Algeria•           {red}03–{yellow}•Andorra•           {red}04–{yellow}•Angola•
            {red}05–{yellow}•Antigua & Barbuda•  {red}06–{yellow}•Argentina•         {red}07–{yellow}•Armenia•           {red}08–{yellow}•Aruba•
            {red}09–{yellow}•Australia•          {red}10–{yellow}•Austria•           {red}11–{yellow}•Azerbaijan•        {red}12–{yellow}•The Bahamas•
            {red}13–{yellow}•Bangladesh•         {red}14–{yellow}•Barbados•          {red}15–{yellow}•Belarus•           {red}16–{yellow}•Belgium•
            {red}17–{yellow}•Benin•             {red}18–{yellow}•Bosnia and Herzegovina• {red}19–{yellow}•Botswana•      {red}20–{yellow}•Brazil•
            {red}21–{yellow}•Bulgaria•           {red}22–{yellow}•Cambodia•           {red}23–{yellow}•Canada•            {red}24–{yellow}•Cayman Islands•
            {red}25–{yellow}•Chile•              {red}26–{yellow}•China•             {red}27–{yellow}•Congo•             {red}28–{yellow}•Costa Rica•
            {red}29–{yellow}•Côte d'Ivoire•      {red}30–{yellow}•Croatia•           {red}31–{yellow}•Cyprus•            {red}32–{yellow}•Czech Republic•
            {red}33–{yellow}•Denmark•            {red}34–{yellow}•Egypt•             {red}35–{yellow}•El Salvador•       {red}36–{yellow}•Faeroe Islands•
            {red}37–{yellow}•Finland•            {red}38–{yellow}•France•            {red}39–{yellow}•Gabon•             {red}40–{yellow}•Georgia•
            {red}41–{yellow}•Germany•            {red}42–{yellow}•Gibraltar•         {red}43–{yellow}•Greece•            {red}44–{yellow}•Guadeloupe•
            {red}45–{yellow}•Guam•               {red}46–{yellow}•Guatemala•         {red}47–{yellow}•Guyana•            {red}48–{yellow}•Honduras•
            {red}49–{yellow}•Hong Kong•          {red}50–{yellow}•Hungary•           {red}51–{yellow}•India•             {red}52–{yellow}•Indonesia•
            {red}53–{yellow}•Iran•               {red}54–{yellow}•Ireland•           {red}55–{yellow}•Israel•            {red}56–{yellow}•Italy•
            {red}57–{yellow}•Jamaica•            {red}58–{yellow}•Japan•             {red}59–{yellow}•Jordan•            {red}60–{yellow}•Kazakhstan•
            {red}61–{yellow}•Kenya•              {red}62–{yellow}•Kuwait•            {red}63–{yellow}•Laos•              {red}64–{yellow}•Lebanon•
            {red}65–{yellow}•Liechtenstein•      {red}66–{yellow}•Luxembourg•        {red}67–{yellow}•Macau•             {red}68–{yellow}•Macedonia•
            {red}69–{yellow}•Madagascar•         {red}70–{yellow}•Malaysia•          {red}71–{yellow}•Malta•             {red}72–{yellow}•Martinique•
            {red}73–{yellow}•Mauritius•          {red}74–{yellow}•Mexico•            {red}75–{yellow}•Moldova•           {red}76–{yellow}•Mongolia•
            {red}77–{yellow}•Morocco•            {red}78–{yellow}•Namibia•           {red}79–{yellow}•Nepal•             {red}80–{yellow}•Netherlands•
            {red}81–{yellow}•New Caledonia•      {red}82–{yellow}•New Zealand•       {red}83–{yellow}•Nicaragua•         {red}84–{yellow}•Nigeria•
            {red}85–{yellow}•Norway•             {red}86–{yellow}•Pakistan•          {red}87–{yellow}•Panama•            {red}88–{yellow}•Paraguay•
            {red}89–{yellow}•Peru•               {red}90–{yellow}•Philippines•       {red}91–{yellow}•Poland•            {red}92–{yellow}•Portugal•
            {red}93–{yellow}•Puerto Rico•        {red}94–{yellow}•Qatar•            {red}95–{yellow}•Réunion•           {red}96–{yellow}•Romania•
            {red}97–{yellow}•Russia•             {red}98–{yellow}•Saint Kitts & Nevis• {red}99–{yellow}•Saint Vincent•   {red}100–{yellow}•São Tomé•
            {red}101–{yellow}•Saudi Arabia•       {red}102–{yellow}•Senegal•         {red}103–{yellow}•Slovakia•         {red}104–{yellow}•South Africa•
            {red}105–{yellow}•South Korea•       {red}106–{yellow}•Spain•           {red}107–{yellow}•Sri Lanka•        {red}108–{yellow}•Sudan•
            {red}109–{yellow}•Suriname•          {red}110–{yellow}•Sweden•          {red}111–{yellow}•Switzerland•      {red}112–{yellow}•Syria•
            {red}113–{yellow}•Taiwan•            {red}114–{yellow}•Tanzania•        {red}115–{yellow}•Thailand•         {red}116–{yellow}•Trinidad and Tobago•
            {red}117–{yellow}•Tunisia•           {red}118–{yellow}•Turkey•          {red}119–{yellow}•U-A-Emirates•     {red}120–{yellow}•Uganda•
            {red}121–{yellow}•Ukraine•           {red}122–{yellow}•United Kingdom•  {red}123–{yellow}•United States•    {red}124–{yellow}•Uruguay•
            {red}125–{yellow}•Uzbekistan•        {red}126–{yellow}•Vietnam•

            {red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺""")
                break
                # Corresponding country codes in alphabetical order
            gamer="human"
            try :
                type_text(text1)
                countries = ["AL","DZ","AD","AO", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BD", "BB", 
                    "BY", "BE", "BJ", "BA", "BW", "BR", "BG", "KH", "CA", "KY", "CL", "CN", "CG", "CR", 
                    "CI", "HR", "CY", "CZ", "DK", "EG", "SV", "FO", "FI", "FR", "GA", "GE", "DE", "GI", 
                    "GR", "GP", "GU", "GT", "GY", "HN", "HK", "HU", "IN", "ID", "IR", "IE", "IL", "IT", 
                    "JM", "JP", "JO", "KZ", "KE", "KW", "LA", "LB", "LI", "LU", "MO", "MK", "MG", "MY", 
                    "MT", "MQ", "MU", "MX", "MD", "MN", "MA", "NA", "NP", "NL", "NC", "NZ", "NI", "NG", 
                    "NO", "PK", "PA", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "KN", 
                    "VC", "ST", "SA", "SN", "SK", "ZA", "KR", "ES", "LK", "SD", "SR", "SE", "CH", "SY", 
                    "TW", "TZ", "TH", "TT", "TN", "TR", "AE", "UG", "UA", "GB", "US", "UY", "UZ", "VN"]


                headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36"}
                num = int(input(f"{yellow}[?]~>{red}Enter code country : "))
                if num not in range(1,128):
                    raise IndexError

                text=""
                country = countries[num-1]
                res = requests.get( f"http://www.insecam.org/en/bycountry/{country}",headers=headers )
                last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get( f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers )
                    find_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", res.text)
                    print(f"""\n{bold+yellow}@Mohammadmahdi_termux""")
                    print(green+"")

                    for ip in find_ip:
                        print(ip)



            except:

                        print(red+" !ERORR❌ ")


        elif choice == 4:
            clear_terminal()
            import requests
            import re
            import colorama
            colorama.init()
            import os
            import sys
            import time
            green  ="\x1b[1;92m"
            cyan   ="\x1b[1;96m"
            yellow ="\x1b[1;93m"
            magenta   ="\x1b[1;95m"
            white  ="\x1b[1;97m"
            blue   ="\x1b[1;94m"
            red  ='\x1b[1;91m'
            underline = '\033[4m'
            pink = '\033[35m'
            bold = '\033[1m'
            black='\033[30m'


            def type_text(text):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.001)
                print()                  
            text = (f"""{green}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
            ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
            ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
            ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            {yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

            {green}[<ID~>github] ▪︎  {white}https://github.com/mohammadmahdi-termux
            {cyan}[<ID~>telegram] ▪︎  {white}@Mohammadmahdi_termux
            {magenta}[<ID~>instagram] ▪︎  {white}@Mohammadmahditermux

            {red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺
                {red}01–{green}Dlink        {red}02–{green}DLink-DCS-932  {red}03– {green}TPLink        {red}04–{green}Foscam
                {red}05–{green}Linksys      {red}06–{green}Sony           {red}07–{green}Sony-CS3       {red}08–{green}Vije
                {red}09–{green}Mobotix      {red}10–{green}Panasonic      {red}11–{green}Megapixel      {red}12–{green}ChannelVision

            {red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺""")

            try :
                type_text(text)

                MFs = ["DLink","DLink-DCS-932","TPLink","Foscam","Linksys","Sony","Sony-CS3","Vije","Mobotix","Panasonic","Megapixel" ,"ChannelVision"]


                headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36"}
                num = int(input(f"{yellow}[?]~>{red}Enter a number : "))
                if num not in range(1, 13):
                    raise IndexError

                text= ""    
                MF = MFs[num-1]
                res = requests.get( f"http://www.insecam.org/en/bytype/{MF}",headers=headers )

                last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

                for page in range(int(last_page)):

                    res = requests.get( f"http://www.insecam.org/en/bytype/{MF}/?page={page}", headers=headers )

                    find_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", res.text)
                    print(f"""\n{bold+yellow}@Mohammadmahdi_termux""")
                    print(green+"")

                    for ip in find_ip:
                        print(ip)
            except:
                        print(red+" !ERORR❌ ")
    else:
        print(f"""{red}Please enter a number""")
    # To go back to the first house
    go_back = input(f"""{bold}{yellow}Do you want to step out of the tool?!  {green}n{white} / {red}y{blue} {white}: """)
    if go_back.lower() not in ['no', 'n']:
        print(f"""{red}Thanks for choosing me, don't forget to {yellow}star⭐️""")
        break
    else:
        clear_terminal()