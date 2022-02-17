from function import *
from aiogram import types
from notes_bot import dp, bot
import datetime as dt
import keyboards as kb
import text


@dp.callback_query_handler(lambda c: c.data == 'edit_today' or c.data == 'edit__tomorrow')
async def editNotes(call: types.CallbackQuery):
    """ Редактирование списка событий """
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    userid = call.from_user.id
    date = dt.datetime.strptime(dateNowStr(), '%d.%m.%Y')
    await bot.answer_callback_query(call.id, text.ed1)
    if call.data == 'edit_today':
        mess = text.ed2 + date.strftime("%d.%m.%y") + '*'
        mess += text.ed3
        await call.message.edit_text(mess, parse_mode="Markdown")
        cur.execute('SELECT * FROM notes where userid = ? and date = ? ORDER BY time ASC',
                    [userid, date.timestamp()])
        result = cur.fetchall()
        if len(result) == 0:
            await call.message.answer('Список пуст!')
        else:
            for note in result:
                mess = '*'
                if note[5] == 1:
                    mess += u'\U000026A1 '
                mess += dt.datetime.fromtimestamp(note[3]).strftime('%H:%M') + '* '
                mess += note[4]
                await call.message.answer(mess, parse_mode="Markdown", reply_markup=kb.edit(note[0]))
    elif call.data == 'edit__tomorrow':
        mess = text.ed4
        mess += text.ed5
        await call.message.edit_text(mess, parse_mode="Markdown")
        cur.execute('SELECT * FROM notes where userid = ? and date = ? ORDER BY time ASC',
                    [userid, date.timestamp()+86400])
        result = cur.fetchall()
        if len(result) == 0:
            await call.message.answer('Список пуст!')
        else:
            for note in result:
                mess = '*'
                if note[5] == 1:
                    mess += u'\U000026A1 '
                mess += dt.datetime.fromtimestamp(note[3]).strftime('%H:%M') + '* '
                mess += note[4]
                await call.message.answer(mess, parse_mode="Markdown", reply_markup=kb.edit(note[0]))
    else:
        pass
