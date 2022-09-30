from UI import Options,Header
from colorama import Fore
from Action import Searching

Reset = Fore.WHITE

def Acting():
    while True:
        Header.HeaderBanner()
        Options.GetUrlOptions()
        
        try:
            GetUrlInput = input(Fore.RED+" ┌──{"+Fore.BLUE+"IP-FINDER"+Fore.RED+"}"+Fore.CYAN+"==>"+Fore.RED+"["+Fore.LIGHTGREEN_EX+"Home"+Fore.CYAN+"/"+Fore.LIGHTGREEN_EX+"Url"+Fore.RED+"]""""
 └─"""+Fore.CYAN+"$ "+Reset)
            
            if GetUrlInput.count("http://") > 0:
                pass
            elif GetUrlInput.count("https://") > 0:
                pass
            elif GetUrlInput.count("www.") > 0:
                pass
            elif GetUrlInput.count(".") < 1:
                pass
            elif GetUrlInput.count("#") > 0:
                pass
            elif GetUrlInput.count("@") > 0:
                pass
            elif GetUrlInput.count("$") > 0:
                pass
            elif GetUrlInput.count("%") > 0:
                pass
            elif GetUrlInput.count("!") > 0:
                pass
            elif GetUrlInput.count("&") > 0:
                pass
            elif GetUrlInput.count("*") > 0:
                pass
            elif GetUrlInput.count("(") > 0:
                pass
            elif GetUrlInput.count(")") > 0:
                pass
            elif GetUrlInput.count("[") > 0:
                pass
            elif GetUrlInput.count("]") > 0:
                pass
            elif GetUrlInput.count("{") > 0:
                pass
            elif GetUrlInput.count("}") > 0:
                pass
            elif GetUrlInput.count("|") > 0:
                pass
            elif GetUrlInput.count("/") > 0:
                pass
            elif GetUrlInput.count("?") > 0:
                pass
            elif GetUrlInput.count(",") > 0:
                pass
            elif GetUrlInput.count("`") > 0:
                pass
            else:
                Searching.Search(GetUrlInput)
            
        except KeyboardInterrupt:
            exit(Fore.RED+"\n\n [IP-FINDER] Was Killed . . .")