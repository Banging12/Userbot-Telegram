from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, BOT_USERNAME
from userbot.events import register


@register(outgoing=True, pattern=r"^\.inlineon(?: |$)(.*)")
async def _(event):
    await event.edit(f"Sedang menyalakan inline untuk @{BOT_USERNAME} tunggu sebentar")
            async with bot.conversation("@BotFather") as conv:
                try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
                    await conv.send_message("/setinline")
                    await conv.get_response()
                    await conv.send_message(f"@{BOT_USERNAME}")
                    await conv.get_response()
                    await conv.send_message("Search")
                    await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await event.edit("Unblock @Botfather first.")
                await event.edit(
                    "**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `.helpme` **lagi untuk membuka menu bantuan.**"
                )
            )
