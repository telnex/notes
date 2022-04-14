from function import *
from aiogram import types
from notes_bot import dp
from aiogram.dispatcher.filters.builtin import Text
import keyboards as kb
import datetime as dt


@dp.callback_query_handler(Text('today'))
@dp.callback_query_handler(Text('imp_today'))
async def today(call: types.CallbackQuery):
    """ Отображение событий текущего дня """
    if call.data == 'imp_today':
        await call.answer(text.td1)
    else:
        await call.answer()
    userid = call.from_user.id
    date = dt.datetime.strptime(dateNowStr(), '%d.%m.%Y')
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    if call.data == 'imp_today':
        mess = text.td2 + date.strftime("%d.%m.%y") + text.td3
        cur.execute('SELECT * FROM notes where userid = ? and date = ? and imp = 1 ORDER BY time ASC', [userid, date.timestamp()])
        keyboard = kb.today(2)
    else:
        mess = text.td4 + date.strftime("%d.%m.%y") + '*\n'
        cur.execute('SELECT * FROM notes where userid = ? and date = ? ORDER BY time ASC', [userid, date.timestamp()])
        keyboard = kb.today(1)
    result = cur.fetchall()
    if len(result) == 0:
        if call.data == 'imp_next':
            mess += text.td5
        else:
            mess += text.td6
        await call.message.edit_text(mess, parse_mode="Markdown", reply_markup=kb.today(0))
    else:
        for data in result:
            mess += '\n*' + dt.datetime.fromtimestamp(data[3]).strftime('%H:%M') + '* ' + data[4]
        await call.message.edit_text(mess, parse_mode="Markdown", reply_markup=keyboard)



