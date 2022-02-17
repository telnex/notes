import keyboards as kb
from function import *
from aiogram import types
from notes_bot import dp


@dp.message_handler(commands="control")
async def adminControl(message: types.Message):
    """ Админ панель """
    if message.chat.id == admin:
        mess = text.adm1
        mess += '```python3'
        mess += getLog()
        mess += '```'
        await message.answer(mess, parse_mode="Markdown", reply_markup=kb.download_log)
        mess = text.adm2
        mess += str(qCountUser())
        mess += text.adm3
        mess += str(qCountNotes())
        await message.answer(mess, parse_mode="Markdown")

