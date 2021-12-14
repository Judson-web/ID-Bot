from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from MT_ID_Bot.Translation import Translation
from MT_ID_Bot.Config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

@MT_ID_Bot.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sᴏʀʀʏ Dᴜᴅᴇ, Yᴏᴜ ᴀʀᴇ**🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"Jᴏɪɴ", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"Tʀʏ", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"@{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<u>Fᴏʀᴡᴀʀᴅ Iɴғᴏʀᴍᴀᴛɪᴏɴ 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 Bᴏᴛ Iɴғᴏ</u>"
        else:
            text += "<u>👤Usᴇʀ Iɴғᴏ</u>"
        text += f'\n\n👨‍💼 Nᴀᴍᴇ : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n🔗 Usᴇʀɴᴀᴍᴇ : @{msg.forward_from["username"]} \n\n🆔 ɪᴅ : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 ɪᴅ : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️Eʀʀᴏʀ <b><i>{hidden}</i></b> ❌️Eʀʀᴏʀ",
                quote=True,
            )
        else:
            text = f"<u>Fᴏʀᴡᴀʀᴅ Iɴғᴏʀᴍᴀᴛɪᴏɴ 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 Cʜᴀɴɴᴇʟ</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ Gʀᴏᴜᴘ</u>"
            text += f'\n\n💼 Nᴀᴍᴇ {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n➡️ Fʀᴏᴍ : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 ɪᴅ : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 ɪᴅ : `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
