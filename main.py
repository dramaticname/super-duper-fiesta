import httpx
import proxy_processor
from itertools import cycle
import ctypes
from msvcrt import getch
ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Joiner")

invite = input('Invite: ')
if len(link) > 6:
    link = link[19:]

api = "https://discordapp.com/api/v9/invite/" + invite

with open('tokens.txt', 'r') as uwu:
    tokens = uwu.readlines()
    for token in tokens:
        rstrip = token.rstrip()
        headers = {'Authorization': rstrip}
        httpx.get(api, headers=headers, proxies={"https://': 'http://" + proxy_processor.GetProxies()})

print("Done!")
print("Press any key to exit...")
junk = getch()
