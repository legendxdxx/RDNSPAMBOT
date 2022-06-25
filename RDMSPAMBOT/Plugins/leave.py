import asyncio
from RDMSPAMBOT import Rdn, Rdn2, Rdn3, Rdn4, Rdn5, Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, SUDO_USERS
from RDMSPAMBOT import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys

@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        Rdnspam = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = Rdnspam[0]
            Xd = int(bc)
            text = "Leaving....."
            event = await e.reply(text)
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("Succesfully Left !! ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "I'm Leaving This Group......"
             if e.is_private:
                  dik = f"You Can't Do This Here !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : type in the group, bot will auto leave that group..!"
                  await e.reply(dik)
             else:
                  event = await e.reply(text)
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))
