from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

I can help you to do stuff on PDFs as well as convert images to PDF. Use /help to see features.

Just Send A PDF or image to get started.

Made With❤️By @M2Botz
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("💬 Update Channel", url="https://t.me/m2botz"),
            InlineKeyboardButton("🗣 Support Group", url="https://t.me/m2botzsupport")
        ],
           [InlineKeyboardButton("🧑‍💻Developer", url="https://t.me/ask_admin01")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" About 😎", callback_data="about")
        ],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/m2botz/17")],
    ]

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot with PDF Tools by @StarkBots

🌐Source Code : [Releasing Soon](https://t.me/m2botz)

💬 Update Channel : [Join](https://t.me/m2botz)

🗣 Support Group : [Join](https://t.me/m2botzsupport)

🧑‍💻Developer : [M2](https://t.me/ask_admin01)
    """
