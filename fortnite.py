try:
    # System imports.
    import asyncio
    import json
    import logging
    import sys
    import datetime
    import subprocess
    import os
    import time
    import requests
    import crayons
    import webbrowser
    import json
    # Third party imports.
    import aiofiles
    import fortnitepy
    import crayons
    import subprocess
    import aiohttp


async def main() -> None:
    if data['path'] == "":
            path = input(f"{crayons.cyan('[+] Please Enter The Location Where Fortnite Is Installed: ', bold=True)}")
            data['path'] = path
            location = f"{path}\FortniteGame\Binaries\Win64"
            os.replace("cache/FortniteClient-Win64-Shipping_BE.exe", f"{location}\FortniteClient-Win64-Shipping_BE.exe")
            os.replace("cache/FortniteClient-Win64-Shipping_EAC.exe", f"{location}\FortniteClient-Win64-Shipping_EAC.exe")
            os.replace("cache/ssl.dll", f"{location}\ssl.dll")
            print(f"{crayons.cyan('[+] Launching Fortnite...', bold=True)}")
            gen = partybot.EpicGenerator()
            subprocess.call([f'{path}\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping'])
            print(f"{crayons.cyan('[+] Launched Fortnite!', bold=True)}")
            time.sleep(5)