from Rdmspambot import Rdn, Rdn2, Rdn3, Rdn4, Rdn5, Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, SUDO_USERS
from telethon import events, Button
from Rdmspambot import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/81c502daf64192d9d54eb.jpg"

RdnHelp = "โ ๐ฅ๐๐ก ๐ฆ๐ฃ๐๐  ๐๐๐๐ฃ โ\n๐๐ฅ๐ข๐๐ค ๐๐ง ๐๐๐ฅ๐จ๐ฐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐จ๐ซ ๐๐๐ฅ๐ฉ\n\n\n@Kartik_king01"


@Rdn.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Rdn10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RdnHelp,
                                  buttons=[
           [
            Button.inline("๐ฅ Spam ๐ฅ", data="spam"),
            Button.inline("๐ Raid ๐", data="raid"),
           ],
           [
            Button.inline("โก Extra โก", data="extra"),
           ],
           [    
            Button.url("โจ แดสแดษดษดแดส โจ", "https://t.me/RMWNETWORK")
           ],
           [
           Button.url("โจ sแดแดแดแดสแด โจ", "https://t.me/RDNNETWORK")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**
**UserBot :** Userbot Cmds
Command :
1) {hl}ping 
2) {hl}alive
3) {hl}restart
4) {hl}addsudo <reply to user> || Owner Cmd ||
5) {hl}logs || Owner Cmd ||
**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>
**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group
**PackSpam :** Sticker Pack Spam
1) {hl}packspam <reply to any sticker>
**ยฉ @KARTIK_KING01**
"""

                 
raid_msg = f"""
**Help Raid Cmds**
**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>
**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>
**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>
**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>
**ยฉ @KARTIK_KING01**
"""

spam_msg = f"""
**Help Spam Cmds**
**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>
**BigSpam :** Spams a Message For Given Counter.
Command :
1) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}bigspam <count> <replying any message>
**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>
**PormSpam :** Pormography Spam.
Command :
1) {hl}pornspam <count>
**Hang :** Spams Hanging Message For Given Counter.
Command :
1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)
** ยฉ @KARTIK_KING01**
"""                     
           
           
@Rdn.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn2.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn3.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn4.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn5.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn6.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn7.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn8.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn9.on(events.CallbackQuery(pattern=r"help_back"))
@Rdn10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            RdnHelp,
            buttons=[
           [
            Button.inline("๐ฅ Spam ๐ฅ", data="spam"),
            Button.inline("๐ Raid ๐", data="raid"),
           ],
           [
            Button.inline("โก Extra โก", data="extra"),
           ],
           [    
            Button.url("โจ แดสแดษดษดแดส โจ", "https://t.me/RMWNETWORK")
           ],
           [
           Button.url("โจ sแดแดแดแดสแด โจ", "https://t.me/RDNNETWORK")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your OwN RDN Spam Bots !! @ROYALYSERBOT "
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Rdn.on(events.CallbackQuery(pattern=r"spam"))
@Rdn2.on(events.CallbackQuery(pattern=r"spam"))
@Rdn3.on(events.CallbackQuery(pattern=r"spam"))
@Rdn4.on(events.CallbackQuery(pattern=r"spam"))
@Rdn5.on(events.CallbackQuery(pattern=r"spam"))
@Rdn6.on(events.CallbackQuery(pattern=r"spam"))
@Rdn7.on(events.CallbackQuery(pattern=r"spam"))
@Rdn8.on(events.CallbackQuery(pattern=r"spam"))
@Rdn9.on(events.CallbackQuery(pattern=r"spam"))
@Rdn10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your OwN RDN Spam Bots !! @ROYALYSERBOT"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Rdn.on(events.CallbackQuery(pattern=r"raid"))
@Rdn2.on(events.CallbackQuery(pattern=r"raid"))
@Rdn3.on(events.CallbackQuery(pattern=r"raid"))
@Rdn4.on(events.CallbackQuery(pattern=r"raid"))
@Rdn5.on(events.CallbackQuery(pattern=r"raid"))
@Rdn6.on(events.CallbackQuery(pattern=r"raid"))
@Rdn7.on(events.CallbackQuery(pattern=r"raid"))
@Rdn8.on(events.CallbackQuery(pattern=r"raid"))
@Rdn9.on(events.CallbackQuery(pattern=r"raid"))
@Rdn10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your OwN RDN Spam Bots !! @ROYALYSERBOT"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Rdn.on(events.CallbackQuery(pattern=r"extra"))
@Rdn2.on(events.CallbackQuery(pattern=r"extra"))
@Rdn3.on(events.CallbackQuery(pattern=r"extra"))
@Rdn4.on(events.CallbackQuery(pattern=r"extra"))
@Rdn5.on(events.CallbackQuery(pattern=r"extra"))
@Rdn6.on(events.CallbackQuery(pattern=r"extra"))
@Rdn7.on(events.CallbackQuery(pattern=r"extra"))
@Rdn8.on(events.CallbackQuery(pattern=r"extra"))
@Rdn9.on(events.CallbackQuery(pattern=r"extra"))
@Rdn10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your OwN RDN Spam Bots !! @ROYALYSERBOT"
            )
        await event.answer(Alert, cache_time=0, alert=True)
