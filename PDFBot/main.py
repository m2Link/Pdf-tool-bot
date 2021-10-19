from pyrogram import Client, filters
from PDFBot.core import extract_info
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from PyPDF2.pdf import PdfFileReader
import warnings

merging = {}


@Client.on_message(filters.private & filters.document & filters.incoming)
async def main(_, msg: Message):
    user_id = msg.from_user.id
    warnings.filterwarnings("ignore")  # Too much warnings
    if not msg.document.file_name.endswith(".pdf"):
        return
    if user_id in merging and merging[user_id]:
        return
    status = await msg.reply("Downloading PDF...", quote=True)
    pdf = await msg.download(file_name=f"downloads/{msg.from_user.id}/1.pdf")
    pdf_object = PdfFileReader(pdf)
    info = extract_info(pdf)
    buttons = [
        [InlineKeyboardButton("Rotate PDF", callback_data="rotate")],
        [InlineKeyboardButton("Merge PDFs", callback_data="merge")],
        [InlineKeyboardButton("Extract Text from PDF", callback_data="extract")],
        [InlineKeyboardButton("Split PDF", callback_data="split")]
    ]
    if pdf_object.isEncrypted:
        buttons = [[InlineKeyboardButton("Decrypt PDF", callback_data="decrypt")]]
    else:
        buttons.insert(0, [InlineKeyboardButton("Encrypt PDF", callback_data="encrypt")])
    await status.delete()
    if "decrypted file back" in info:
        await msg.reply(
            f"**Encrypted File** \n\n{info} \n\nUse Below Button To Decrypt The Pdf File.",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await msg.reply(
            f"**PDF Information** \n\n{info} \n\nUse Below Buttons To Act On The Pdf File.",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
