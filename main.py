import os

os.system("clear")

def main():
    print ("")
    print ('''
\033[1;34m██   ██  █████  ██      ██
\033[1;34m██  ██  ██   ██ ██      ██
\033[1;34m█████   ███████ ██      ██
\033[1;34m██  ██  ██   ██ ██      ██
\033[1;34m██   ██ ██   ██ ███████ ██
\033[1;37m
██      ██ ███   ██ ██    ██ ██   ██
██      ██ ████  ██ ██    ██  ██ ██
██      ██ ██ ██ ██ ██    ██   ███
██      ██ ██  ████ ██    ██  ██ ██
███████ ██ ██   ███  ██████  ██   ██''')
    print ("")
    print ("\033[1;31m[1]\033[1;32mStart kali Linux ")
    print ("\033[1;31m[2]\033[1;32mUpdate")
    print ("\033[1;31m[3]\033[1;32mExit")
    print ("")
    x=int(input("\033[1;31m[●]\033[1;33mEnter Your Choice \033[1;31m》》\033[1;37m:"))
    if x==1:
       os.system("clear")
       os.system("./install-nethunter-termux")
       os.system("nethunter")
    elif x==2:
         os.system("clear")
         os.system("apt update && apt upgrade -y")
         os.system("apt install nano -y")
         os.system("termux-setup-storage")
         os.system("apt install wget")
         os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
         os.system("chmod +x install-nethunter-termux")
         os.system("clear")
         main()
    elif x==3:
         os.system("clear")
    else:
         print ("not .../")
main()
