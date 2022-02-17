from function import *
from aiogram import types
from notes_bot import dp, bot
import keyboards as kb
import datetime as dt


@dp.callback_query_handler(lambda c: c.data == 'tomorrow' or c.data == 'imp_tomorrow')
async def tomorrow(call: types.CallbackQuery):
    """ Отображение событий следующего дня """
    if call.data == 'imp_tomorrow':
        await bot.answer_callback_query(call.id, text.tm1)
    else:
        await bot.answer_callback_query(call.id)
    userid = call.from_user.id
    date = dt.datetime.strptime(dateNowStr(), '%d.%m.%Y')
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    if call.data == 'imp_tomorrow':
        mess = text.tm2
        cur.execute('SELECT * FROM notes where userid = ? and date = ? and imp = 1 ORDER BY time ASC',
                    [userid, date.timestamp()+86400])
        keyboard = kb.tomorrow(2)
    else:
        mess = text.tm3
        cur.execute('SELECT * FROM notes where userid = ? and date = ? ORDER BY time ASC',
                    [userid, date.timestamp()+86400])
        keyboard = kb.tomorrow(1)
    result = cur.fetchall()
    if len(result) == 0:
        if call.data == 'imp_tomorrow':
            mess += text.tm4
        else:
            mess += text.tm5
        await call.message.edit_text(mess, parse_mode="Markdown", reply_markup=keyboard)
    else:
        for data in result:
            mess += '\n*' + dt.datetime.fromtimestamp(data[3]).strftime('%H:%M') + '* ' + data[4]
        await call.message.edit_text(mess, parse_mode="Markdown", reply_markup=keyboard)



