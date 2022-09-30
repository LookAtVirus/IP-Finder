import platform
import os

def Check():
    PL = platform.uname()[0]
    if PL == "Windows":
        exit("\nSorry, This is For Linux Platform, We Don't Support Windows ! ! !")
    else:
        pass
    
    if os.geteuid() != 0:
        exit("\nPlease Run The Program as Root ! ! !")
    else:
        pass
    
    try:
        import colorama
        import requests

    except ImportError:
        exit("\nPlease Install Libraries --> python3 -m pip install -r requirments.txt")
    
    try:
        requests.get("https://www.google.com")
    except:
        exit("\nPlease Check Your Netork Connection . . .")