from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Rkn_Bots as Config
from .database import insert

async def not_subscribed(_, client, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    if not Config.FORCE_SUB:
        return False
        
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="📢 Join Update Channel 📢", url=f"https://t.me/{Config.FORCE_SUB}") ]]
    text = "**Sᴏʀʀy Dᴜᴅᴇ you did Nᴏᴛ Jᴏɪɴ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ 'Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ' Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ**"
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ #nikl laude ")  
        elif user.status == enums.ChatMemberStatus.LEFT:
            return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          
