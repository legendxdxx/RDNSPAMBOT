from Rdmspam import Rdn, Rdn2, Rdn3, Rdn4, Rdn5, Rdn6, Rdn7, Rdn8, Rdn9, Rdn10, SUDO_USERS
from telethon import events, Button
from Rdmspam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/81c502daf64192d9d54eb.jpg"

RdnHelp = "★ 𝗥𝗗𝗡 𝗦𝗣𝗔𝗠 𝗛𝗘𝗟𝗣 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩\n\n\n@Kartik_king01"


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
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/RMWNETWORK")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/RDNNETWORK")
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
**© @KARTIK_KING01**
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
**© @KARTIK_KING01**
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
** © @KARTIK_KING01**
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
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/RMWNETWORK")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/RDNNETWORK")
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
       


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
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
