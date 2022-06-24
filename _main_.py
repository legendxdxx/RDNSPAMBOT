import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from RDNSPAMBOT.utils import load_plugins
import logging
from telethon import events
from . import Rdn, Rdn2, Rdn3, Rdn4, Rdn5, Rdn6, Rdn7, Rdn8, Rdn9, Rdn10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RDNSPAMBOT/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Mighty X BotSpam Successfully Deployed !!")
print("Enjoy..!  Support @RMWNETWORK ")

if __name__ == "__main__":
    Rdn.run_until_disconnected()
    
if __name__ == "__main__":
    Rdn2.run_until_disconnected()

if __name__ == "__main__":
    Rdn3.run_until_disconnected()
    
if __name__ == "__main__":
    Rdn4.run_until_disconnected()

if __name__ == "__main__":
    Rdn5.run_until_disconnected()
    
if __name__ == "__main__":
    Rdn6.run_until_disconnected()
    
if __name__ == "__main__":
    Rdn7.run_until_disconnected()

if __name__ == "__main__":
    Rdn8.run_until_disconnected()
    
if __name__ == "__main__":
    Rdn9.run_until_disconnected()

if __name__ == "__main__":
    Rdn10.run_until_disconnected()    
