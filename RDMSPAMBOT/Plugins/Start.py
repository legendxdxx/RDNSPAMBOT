import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Mig, Mig2, Mig3, Mig4, Mig5, Mig6, Mig7, Mig8, Mig9, Mig10, ALIVE_PIC, OWNER_ID
from MightyXSpam.plugins.help import *


MIG_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/0cb63f5f5b0cbb6a559f0.jpg"

Mig_Button = [
        [
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/RMWNETWORK ")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
MigX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/ROYALYSERBOT"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/ROYALUBOT_SUPPORT")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/...?")
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
       MigBot = await event.client.get_me()
       bot_name = RdnBot.first_name
       bot_id = MigBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMighty = event.chat_id
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
                
