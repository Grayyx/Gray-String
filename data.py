from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀᴛʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴩᴩᴏʀᴛ", url="https://t.me/Graymemberr"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/xflsgrayy"),
        ],
    ]

    START = """
**Hey** {},

**This is** {},
**Bot untuk Mengambil String Session!**

**Made With 👑 By:** [ɢʀᴀʏ](https://t.me/xflsgrayy)
—
**Group Support:** [ꜱᴜᴘᴘᴏʀᴛ](https://t.me/Graymemberr)
    """
