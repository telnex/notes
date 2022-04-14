from function import *
from aiogram import types
from notes_bot import dp, bot
from aiogram.dispatcher.filters.builtin import Text
import text


@dp.callback_query_handler(Text(startswith='imp_'))
@dp.callback_query_handler(Text(startswith='del_'))
async def change(call: types.CallbackQuery):
    """ --- """
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    if call.data[:4] == 'imp_':
        await bot.answer_callback_query(call.id, text.ch1)
        cur.execute("""UPDATE notes SET imp = 1 WHERE id = ?;""", [call.data[4:], ])
        connect.commit()
        await call.message.edit_text(f'\U000026A1*{call.message.text}*', parse_mode="Markdown")
    elif call.data[:4] == 'del_':
        await bot.answer_callback_query(call.id, text.ch2)
        cur.execute('DELETE FROM notes WHERE id = ?;', [call.data[4:], ])
        connect.commit()
        await call.message.edit_text(text.ch3, parse_mode="Markdown")
        logging.info(call.from_user.full_name + ' - удалил запись.')
    else:
        pass
