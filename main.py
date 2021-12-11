import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

Pr0fess0r_99 = Client(
    "Ban-and-unban-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

@Pr0fess0r_99.on_message(filters.command(["start"]))
async def start(bot, message):
    await message.reply_text(f"""Hy {message.from_user.mention}\nIam [Ban And UnBan](https://github.com/PR0FESS0R-99/Ban-and-UnBan-Bot) Telegram Bot""")

@Pr0fess0r_99.on_message(filters.command(["ban"]))
async def ban(bot, message):
    chatid = message.chat.id
    if not message.reply_to_message:
        return
    admins_list = await bot.get_chat_members(
        chat_id=chatid, filter="administrators"
    )
    admins = []
    for admin in admins_list:
        id = admin.user.id
        admins.append(id)
    userid = message.from_user.id
    if userid in admins:
        user_to_ban = message.reply_to_message.from_user.id
        if user_to_ban in admins:
            await message.reply(text="Think he is Admin, Can't Ban Admins")
        else:
            try:
                await bot.kick_chat_member(chat_id=chatid, user_id=user_to_ban)
                await message.reply_text(
                    f"Bye {message.reply_to_message.from_user.mention}"
                )
            except Exception as error:
                await message.reply_text(f"{error}")
    else:
        await message.reply_text("Nice try, But wrong move..")
        return

@Pr0fess0r_99.on_message(filters.command(["unban"]))
async def unban(bot, message):
    chatid = message.chat.id
    if not message.reply_to_message:
        return
    admins_list = await bot.get_chat_members(
        chat_id=chatid,
        filter="administrators"
    )
    admins = []
    for admin in admins_list:
        id = admin.user.id
        admins.append(id)
    userid = message.from_user.id
    if userid in admins:
        user_to_unban = message.reply_to_message.from_user.id
        if user_to_uban in admins:
            await message.reply(text="Think he is Admin, Can't Ban Admins")
        else:
            try:
                await bot.unban_chat_member(chat_id=chatid, user_id=user_to_unban)
                await message.reply_text(
                    f"Welcome {message.reply_to_message.from_user.mention}"
                )
            except Exception as error:
                await message.reply_text(f"{error}")
    else:
        await message.reply_text("Nice try, But wrong move..")
        return

Pr0fess0r_99.run()

