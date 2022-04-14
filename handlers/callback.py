from aiogram import types
from notes_bot import dp, bot
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher.filters.builtin import Text


@dp.errors_handler(exception=MessageNotModified)
async def error_bot_blocked(update: types.Update, exception: MessageNotModified):
    """ Обрабатываем исключение: редактирование сообщения исходное=новое"""
    return True

@dp.callback_query_handler(Text('download_log'))
async def download_log(call: types.CallbackQuery):
    """ Скачивание лога """
    await bot.answer_callback_query(call.id)
    txt = types.InputFile('./log/bot.log')
    await bot.send_document(call.from_user.id, txt)