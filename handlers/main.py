import keyboards as kb
import text
from function import *
from aiogram import types
from notes_bot import dp


@dp.message_handler(commands="start")
@dp.message_handler(lambda message: message.text == 'Старт')
async def start(message: types.Message):
    """ Старт """
    if check(message.from_user.id):
        mess = text.start1 + message.from_user.full_name + '!'
        await message.answer(mess, parse_mode="Markdown", reply_markup=kb.keyboard)
        mess = text.start2
        await message.answer(mess, parse_mode="Markdown", reply_markup=kb.home)


@dp.message_handler(commands="help")
async def help(message: types.Message):
    """ Помощь """
    if check(message.from_user.id):
        mess = '!?'
        await message.answer(mess, parse_mode="Markdown")




