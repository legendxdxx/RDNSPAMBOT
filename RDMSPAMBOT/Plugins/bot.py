import os
import asyncio
import sys
import git
import heroku3
from RDMSPAMBOT import Rdn, Rdn2, Rdn3,Rdn4, Rdn5 , Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, mightyversion, mention
from RDMSPAMBOT import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from RDMSPAMBOT import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RDN_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/27dfd474582fb499263d8.jpg"

RDN_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ 
██████╗░██████╗░███╗░░██╗
██╔══██╗██╔══██╗████╗░██║
██████╔╝██║░░██║██╔██╗██║
██╔══██╗██║░░██║██║╚████║
██║░░██║██████╔╝██║░╚███║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝ ★«╝"

                                  
@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
      start = datetime.now()
      text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
      check = await event.reply(text, parse_mode=None, link_preview=None )
      end = datetime.now()
      ms = (end-start).microseconds / 1000
      await check.delete()
      await event.client.send_file(event.chat_id,
                                  RDN_PIC, caption=f"""{MIG_TEXT}\n\n═══════════════════\n⚡ 𝐏𝐢𝐧𝐠  : `{ms}ᵐˢ`\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 : `{mightyversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n═══════════════════\n\n""", buttons=[
        [
        Button.url("✨ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ✨", "https://t.me/ROYALYSERBOT"),
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/ROYALUBOT_SUPPORT")
        ],
        [
        Button.url("🔥 𝗥𝗘𝗣𝗢 🔥", "https://github.com/...?")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝙋𝙤𝙣𝙜!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        message = await event.get_reply_message()
        user = await event.client(GetFullUserRequest(message.sender_id))
        firstname = user.user.first_name
        userid = user.user.id
    if userid == OWNER_ID:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : {mention}")
    else:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={userid})")
        
        

@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your ROYAL SPAM BOT...**\nPlease Wait For Few Seconds."
        await e.reply(text)
        try:
            await Rdn.disconnect()
        except Exception:
            pass
        try:
            await Rdn2.disconnect()
        except Exception:
            pass
        try:
            await Rdn3.disconnect()
        except Exception:
            pass
        try:
            await Rdn4.disconnect()
        except Exception:
            pass
        try:
            await Rdn5.disconnect()
        except Exception:
            pass
        try:
            await Rdn6.disconnect()
        except Exception:
            pass
        try:
            await Rdn7.disconnect()
        except Exception:
            pass
        try:
            await Rdn8.disconnect()
        except Exception:
            pass
        try:
            await Rdn9.disconnect()
        except Exception:
            pass
        try:
            await Rdn10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"__Adding User As Sudo...__")
        Rdnspam = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User !!")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added** `{target}` **As Sudo User** ✨ \nRestarting... Please Wait Few Seconds.")
        heroku_var[Rdnspam] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
