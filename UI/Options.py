from colorama import Fore
import time

Reset = Fore.WHITE

def HomeOptions():
    print(Fore.WHITE+" Please Enter a Word To Choose The Option.\n")
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"i"+Fore.RED+"] "+Fore.LIGHTGREEN_EX+"Search a Website Url to Get Information.\n")
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"e"+Fore.RED+"] "+Fore.RED+"Exit IP-FINDER . . .\n")
    time.sleep(0.1)

def GetUrlOptions():
    print(Fore.RED+" ["+Fore.CYAN+"$"+Fore.RED+"] "+Fore.WHITE+"Please Enter Website Url Example --> "+Fore.LIGHTGREEN_EX+"google.com\n")
    time.sleep(0.1)