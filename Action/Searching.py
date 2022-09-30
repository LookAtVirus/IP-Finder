from UI import Header
import requests
from colorama import Fore
import json
import time

Reset = Fore.WHITE

def Search(URL):
    Header.HeaderBanner()
    try:
        Data = {"get_site_ip" : 1, "input_website" : URL}
        REQ = requests.post("https://get-site-ip.com/inc/icey_ajax.php", data=Data).text
        if REQ.count("<html>") > 0:
            exit(Fore.RED+" [ERROR] "+Fore.WHITE+"You Have Try to Much For Today We Cat Response Your IP Anymore, Tryy Again Later.\n")
        else:
            Reday = json.loads(REQ)
            STC = Reday["geo_data"]["statusCode"]
            Domain = Reday["domain"]
            IP = Reday["geo_data"]["ipAddress"]
            Country = Reday["geo_data"]["countryName"]
            Region = Reday["geo_data"]["regionName"]
            City = Reday["geo_data"]["cityName"]
            Lat = Reday["geo_data"]["latitude"]
            Lon = Reday["geo_data"]["longitude"]
            Link = f"https://www.google.com/maps/place/{Lat}+{Lon}"
            
            if STC == "ERROR":
                print(Fore.RED+" [ERROR] "+Fore.WHITE+"The URL You Sent Have a Problem Searching, We Can't Find "+Fore.RED+"INFO "+Fore.WHITE+"About it.\n")
            else:
                print(Fore.LIGHTGREEN_EX+" [SUCCES] "+Fore.WHITE+"Information Found . . .\n")
                time.sleep(0.1)
                print(Fore.CYAN+" Domain Name"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+Domain+"\n")
                time.sleep(0.1)
                print(Fore.CYAN+" IP Address"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+IP+"\n")
                time.sleep(0.1)
                print(Fore.CYAN+" Country"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+Country+"\n")
                time.sleep(0.1)
                print(Fore.CYAN+" Region"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+Region+"\n")
                time.sleep(0.1)
                print(Fore.CYAN+" City"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+City+"\n")
                time.sleep(0.1)
                print(Fore.CYAN+" Server Location on The Map"+Fore.WHITE+" --> "+Fore.LIGHTGREEN_EX+Link+"\n")
                time.sleep(0.1)
        
        ExitInput = input(Fore.RED+" Do You Want to Try Another Website (y/n) : "+Reset).lower()
        if ExitInput == "y":
            pass
        elif ExitInput == "n":
            exit("\n Have a Nice Day/Night . . .")
        else:
            exit("\n Have a Nice Day/Night . . .")
    except KeyboardInterrupt:
        exit(Fore.RED+"\n\n [IP-FINDER] Was Killed . . .")