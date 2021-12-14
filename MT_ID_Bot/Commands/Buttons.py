from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"t.me/STMbOTsUPPORTgROUP"),
       InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
       ],[
       InlineKeyboardButton("Hᴇʟᴘ", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Tᴇʟᴇɢʀᴀᴍ Iᴅ", callback_data="id"),
       InlineKeyboardButton("Tᴇʟᴇɢʀᴀᴍ Iɴғᴏ", callback_data="info")
       ],[
       InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
       InlineKeyboardButton("Bᴏᴛ Eᴅɪᴛᴏʀ", url=f"t.me/VAMPIRE_KING_NO_1"),
       InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Bᴀᴄᴋ", callback_data="help"),
       InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
       InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
       ]]
       )
