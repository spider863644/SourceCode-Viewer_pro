#!/usr/python3
import os, time as t
#Colors
white = '\033[0;37;40m'
green = '\033[1;32;40m'
redyellow = '\033[1;33;41m'
red = '\033[1;31;40m'
load = '\033[5;31;40m'
cyan = '\033[1;36;40m'
yellow = '\033[1;33;40m'
blue = '\033[1;34;40m'
plus =  "[+]" + green
credit = ['Spider Anongreyhat', 'D3cryptor', 'AnonyminHack5']
t.sleep(1)
os.system("clear")
print(red + "Disclaimer:Use this script for educational purposes only.\n" + redyellow
+ "Spider Anongreyhat" + red + " won\'t be responsible for any shit you used this script for" + white)
t.sleep(3)
os.system("clear")
t.sleep(2)
try:
    print(cyan + "Cheking if requirement has been installed" + load + ".." + white)
    t.sleep(3)
    import requests
    import pyfiglet
  
except ModuleNotFoundError:
    print(red + "Ouch... :( \nSome requirements are  not found!\nBut don\'t worry..requirements will be installed automatically" + white)
    t.sleep(3)
    os.system("clear")
    t.sleep(2)
    print(cyan + "Installing requirements" + load + "..." + white)
    os.system("""
    pip install pyfiglet
    pip install requests
    """)
    print(green + "Run python3 SCV again")
    exit()
print("All done!!!")
t.sleep(2)
os.system("clear")
banner = pyfiglet.figlet_format("SourceCode-Viewer")
def loop():
    os.system('clear')
    print(yellow + banner)
    print(red +"version 2.5".center(60) + white)
    print(yellow + plus + " Tool Name: Source Code Viewer\n" + yellow + plus +  " Creator: Spider Anongreyhat\n" + yellow + plus + " Team: TermuxHackz Society\n" + yellow + plus + " Github: https://github.com/spider863644\n" + yellow + plus + " WhatsApp: +2349052863644" + white)
    print(" ")
    print(blue + """
[1] Get source code of a webpage and save {https  site only}
[2] Get source code of a webpage and save {http sites only}
[3] Update script
[4] Join my WhatsApp group to colabborate with me
[5] Exit Program
""" )
    try:
        choice = int(input(redyellow + "Choose a valid option " + white))
    except ValueError:
        print(red + "Only integers are allowed!" + white)
        t.sleep(1.5)
        loop()
    os.system("clear")
    if choice == 1:
        print(green, credit, white)
        Url = input(redyellow + "Enter the url of the webpage you wanna get its source code " + white)
        filename = input(green + "Enter filename without an extention: ")
        if "https://" not in Url:
            print(red + "Invalid url!")
            t.sleep(2)
            loop()
        url = requests.get(Url)
        os.system("clear")
        print(redyellow + "Getting Source Code of " + Url + load + "..." + white)
        t.sleep(1)
        try:
            file = open(filename + ".html", "x")
        except:
            print(red + "File already exist!")
            t.sleep(3)
            loop()
        file.write((url.text))
        file.close()
        print(blue + url.text)
        print(green + "\n\nFile has been saved as " + filename + ".html")
    elif choice == 2:
        print(green, credit, white)
        Url = input(redyellow + "Enter the url of the webpage you wanna get its source code" + white)
        filename = input(green + "Enter filename: ")
        if "http://" not in Url:
            print(red + "invalid url!" + white)
            t.sleep(4)
            loop()
        url = requests.get(Url)
        os.system("clear")
        print(redyellow + "Getting Source code of " + Url + load + "..." + white)
        t.sleep(1)
        try:
            file = open(filename + ".html", "x")
        except:
            print(red + "File already exist!")
            t.sleep(3)
            loop()
        file.write((url.text))
        file.close()
        print(blue + url.text)
        print(green + "\n\nFile has been saved as " + filename + ".html")
    elif choice == 3:
        os.system("clear")
        t.sleep(4)
        print(redyellow + "Updating Script" + load + "..." + white)
        t.sleep(3)
        os.system("""
        cd
        rm  SourceCode-Viewer_pro
        cd $HOME
        git clone https://github.com/spider863644/SourceCode-Viewer_pro
        """)
        print(cyan + """Type the following Commands below
        cd
        cd SourceCode-Viewer_pro
        """)
        exit()
    elif choice == 4:
        os.system("clear")
        print(redyellow + "Redirecting to my WhatsApp group" + load + "..." + white)
        t.sleep(4)
        os.system("xdg-open https://chat.whatsapp.com/IWqGOsJPjkp2vXcMSJKYns")
        loop()
    elif choice == 5:
        print(red + "Thanks for you using my script\nAllow report any issue you face when using this tool so we can make a better version")
        t.sleep(3)
        exit()
    cont = input(redyellow + "Do you wanna continue?[y/n] " + white)
    if cont == "y" or cont == "Y":
        loop()
loop() 