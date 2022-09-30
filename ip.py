from Dependency import Dep
Dep.Check()
from UI import Header,Options
import os
from colorama import Fore
from Action import Act

Reset = Fore.WHITE
while True:
    Header.HeaderBanner()
    Options.HomeOptions()
    
    try:
        HomeInput = input(Fore.RED+" ┌──{"+Fore.BLUE+"IP-FINDER"+Fore.RED+"}"+Fore.CYAN+"==>"+Fore.RED+"["+Fore.LIGHTGREEN_EX+"Home"+Fore.RED+"]""""
 └─"""+Fore.CYAN+"$ "+Reset).lower()
        
        if HomeInput == "i":
            Act.Acting()
        elif HomeInput == "e":
            exit("\n Have a Nice Day/Night . . .")
        
    except KeyboardInterrupt:
        exit(Fore.RED+"\n\n [IP-FINDER] Was Killed . . .")