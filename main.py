from os import system
mytitle = "The Eroniyom"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

intents = discord.Intents.all()
client = discord.Client(intents=intents)
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

     .-''-.   .-------.         ,-----.     ,---.   .--. .-./`)     ____     __      ,-----.     ,---.    ,---. 
  .'_ _   \  |  _ _   \      .'  .-,  '.   |    \  |  | \ .-.')    \   \   /  /   .'  .-,  '.   |    \  /    | 
 / ( ` )   ' | ( ' )  |     / ,-.|  \ _ \  |  ,  \ |  | / `-' \     \  _. /  '   / ,-.|  \ _ \  |  ,  \/  ,  | 
. (_ o _)  | |(_ o _) /    ;  \  '_ /  | : |  |\_ \|  |  `-'`"`      _( )_ .'   ;  \  '_ /  | : |  |\_   /|  | 
|  (_,_)___| | (_,_).' __  |  _`,/ \ _/  | |  _( )_\  |  .---.   ___(_ o _)'    |  _`,/ \ _/  | |  _( )_/ |  | 
'  \   .---. |  |\ \  |  | : (  '\_/ \   ; | (_ o _)  |  |   |  |   |(_,_)'     : (  '\_/ \   ; | (_ o _) |  | 
 \  `-'    / |  | \ `'   /  \ `"/  \  ) /  |  (_,_)\  |  |   |  |   `-'  /       \ `"/  \  ) /  |  (_,_)  |  | 
  \       /  |  |  \    /    '. \_/``".'   |  |    |  |  |   |   \      /         '. \_/``".'   |  |      |  | 
   `'-..-'   ''-'   `'-'       '-----'     '--'    '--'  '---'    `-..-'            '-----'     '--'      '--' 
                                                                                                               
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: The Eroniyom.{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}

   _______      .---.          ,-----.     ,---.   .--.     .-''-.    ______      
   /   __  \     | ,_|        .'  .-,  '.   |    \  |  |   .'_ _   \  |    _ `''.  
  | ,_/  \__)  ,-./  )       / ,-.|  \ _ \  |  ,  \ |  |  / ( ` )   ' | _ | ) _  \ 
,-./  )        \  '_ '`)    ;  \  '_ /  | : |  |\_ \|  | . (_ o _)  | |( ''_'  ) | 
\  '_ '`)       > (_)  )    |  _`,/ \ _/  | |  _( )_\  | |  (_,_)___| | . (_) `. | 
 > (_)  )  __  (  .  .-'    : (  '\_/ \   ; | (_ o _)  | '  \   .---. |(_    ._) ' 
(  .  .-'_/  )  `-'`-'|___   \ `"/  \  ) /  |  (_,_)\  |  \  `-'    / |  (_.\.' /  
 `-'`-'     /    |        \   '. \_/``".'   |  |    |  |   \       /  |       .'   
   `._____.'     `--------`     '-----'     '--'    '--'    `'-..-'   '-----'`     
                                                                                   

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
