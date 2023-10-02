import os
import requests
from colorama import Fore, Back, Style
import webbrowser
import time


def start():
    welcome = (Fore.RED + "Welcome to my files! Wich one would you like to pick?")
    welcome1 = welcome.center(20)
    print(welcome1)
    print("               ")
    print("[1] - Minecraft")
    print("[2] - CSGO")
    print("[3] - Usefull tools")
    print("                    ")


start()
choice = int(input("Choose:")) 

def choice1():

        print("Choose one of the following:")
        print("[1] - Rise")
        print("[2] - Vape")
        print("[3] - Karma")

        client = str(input("Enter your choice: "))

        if client == "1":
            print("The link is: (Rise Link)")
        elif client == "2":
            print("The link is: (Vape Link)")
        elif client == "3":
            print("The link is: (Karma Link)")
        else:
            print("Invalid choice.")

CSGhost = ("Would you like to open in broswer?")
Osiris = ("Would you like to open in broswer?")


def CSGhost1():
     webbrowser.open("https://www.unknowncheats.me/forum/cs-go-releases/454734-csghost-v4-injector-integrated-vac-bypass.html")

def Osiris1():
     webbrowser.open("https://www.unknowncheats.me/forum/cs-go-releases/454734-csghost-v4-injector-integrated-vac-bypass.html")


CSGhost = ("Would you like to open it on broswer?")
Osiris = ("Would you like to open it on broswer=")

if CSGhost == "yes":
     CSGhost()
else:
     time.sleep(5)
     print("Bye!")
     SystemExit

def choice2():

        print("WARNING: This hacks only on on CSGO 1, they do not work on CSGO 2, i am not responsible for any bans.")
        print("Injector:")
        print("[1] - CSGhost")
        print("DLL:")
        print("[2] - Osiris")

        hack = str(input("Enter your choice: "))

        if hack == "1":
            print("The link is: (CSGhost Link)")
            input(CSGhost)
            
        elif hack == "2":
            print("The link is: (Osiris Link)")
            input(Osiris)
            Osiris1()
        else:
             print("Invalid choice.")

        

def choice3():
        print("Coming soon!")
        

if choice == 1:
    os.system("cls")
    choice1()
elif choice == 2:
    os.system("cls")
    choice2()
elif choice == 3:
    os.system("cls")
    choice3()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
