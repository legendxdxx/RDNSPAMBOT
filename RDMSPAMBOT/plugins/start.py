import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Rdn, Rdn2, Rdn3, Rdn4, Rdn5, Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, ALIVE_PIC, OWNER_ID
from RDMSPAMBOT.plugins.help import *


RDN_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/0cb63f5f5b0cbb6a559f0.jpg"

RDN_Button = [
        [
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/RMWNETWORK ")
        ],
        [
        Button.inline("⚡ DATA ⚡", data="help_back")
        ]
        ]
               
RDN_Button = [
        [
        Button.url("✨ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ✨", "https://t.me/ROYALYSERBOT"),
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/ROYALUBOT_SUPPORT")
        ],
        [
        Button.url("🔥𝗥𝗘𝗣𝗢🔥", "https://github.com/...?")
        ]
        ]
        
        
#USERS 


@Rdn.on(events.NewMessage(pattern="/start"))
@Rdn2.on(events.NewMessage(pattern="/start"))
@Rdn3.on(events.NewMessage(pattern="/start"))
@Rdn4.on(events.NewMessage(pattern="/start"))
@Rdn5.on(events.NewMessage(pattern="/start"))
@Rdn6.on(events.NewMessage(pattern="/start"))
@Rdn7.on(events.NewMessage(pattern="/start"))
@Rdn7.on(events.NewMessage(pattern="/start"))
@Rdn8.on(events.NewMessage(pattern="/start"))
@Rdn9.on(events.NewMessage(pattern="/start"))
@Rdn10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RdnBot = await event.client.get_me()
       bot_name = RdnBot.first_name
       bot_id = RdnBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       RDNFIGHTERS = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From The Button Given Below.** \n\n**Powered By : [𝗥𝗗𝗡 𝗙𝗜𝗚𝗛𝗧𝗘𝗥𝗦 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧](https://t.me/RMWNETWORK)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(RDNFIGHTERS,
                  RDN_IMG,
                  caption=ownermsg, 
                  buttons=RDN_Button)
       else:
            await event.client.send_file(RDNFIGHTERS,
                  RDN_IMG,
                  caption=usermsg, 
                  buttons=RDN_Button)
                
