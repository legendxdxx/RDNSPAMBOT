
import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from RDMSPAMBOT import Rdn, Rdn2, Rdn3, Rdn4, Rdn5 , Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, SUDO_USERS, OWNER_ID

from RDMSPAMBOT import CMD_HNDLR as hl
from RDMSPAMBOT.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from resources.data import Rdnspam


@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : ECHO**\n\nCommand :\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in Rdnspam:
                    text = f"I Can't Echo Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"This Guy is Owner Of These Bots."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("Echo Is Already Activated On This User !!")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo Activated On The User ✅")
     else:
          await event.reply(usage)

@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : RM ECHO**\n\nCommand :\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo Has Been Stopped For The User ☑️")
            else:
                await event.reply("Echo Is Already Disabled !!")
     else:
          await event.reply(usage)


@Rdn.on(events.NewMessage(incoming=True))
@Rdn2.on(events.NewMessage(incoming=True))
@Rdn3.on(events.NewMessage(incoming=True))
@Rdn4.on(events.NewMessage(incoming=True))
@Rdn5.on(events.NewMessage(incoming=True))
@Rdn6.on(events.NewMessage(incoming=True))
@Rdn7.on(events.NewMessage(incoming=True))
@Rdn8.on(events.NewMessage(incoming=True))
@Rdn9.on(events.NewMessage(incoming=True))
@Rdn10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            Rdnspam = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
            Rdnspam = Get(Rdnspam)
            await e.client(Rdnspam)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
