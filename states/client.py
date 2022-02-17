import keyboards as kb
from aiogram import types
from notes_bot import dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from function import *
import datetime as dt


class DataInput(StatesGroup):
    ADD = State()


@dp.message_handler(commands=['cancel'], state='*')
@dp.message_handler(lambda message: message.text == 'Отмена', state='*')
async def setstate_cancel(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()
    await message.answer(text.cancel, parse_mode="Markdown", reply_markup=kb.keyboard)
    logging.warning(message.from_user.full_name + ' - передумал добавлять запись.')


@dp.message_handler(lambda message: message.text == 'Добавить запись')
@dp.message_handler(commands=['add'])
async def set_ADD(message: types.Message):
    if check(message.from_user.id):
        date = dt.datetime.now().strftime("%d.%m.%y")
        mess = text.add1
        mess += text.add2
        mess += '``` '
        mess += date + text.add3
        mess += '```'
        await message.answer(mess, parse_mode="Markdown", reply_markup=kb.cancel)
        await DataInput.ADD.set()


@dp.message_handler(state=DataInput.ADD)
async def addNewNote(message: types.Message, state: FSMContext):
    data = message.text.split('/')
    if len(data) != 3:
        logging.warning('Ошибка .split() строки: len > 3')
        await message.answer('Ошибка! Создайте сообщение строго по шаблону.')
    else:
        date_str = data[0].strip()
        time_str = data[1].strip()
        text_str= data[2].strip()
        try:
            date = dt.datetime.strptime(date_str, '%d.%m.%y')
            tm = dt.datetime.strptime(date_str + ' ' + time_str, '%d.%m.%y %H:%M')
            dttm = dt.datetime.strptime(date_str + ' ' + time_str, '%d.%m.%y %H:%M')
        except Exception as e:
            logging.error('Ошибка с датой! ' + str(e))
            await message.answer('Ошибка! Проверьте правильность ввода даты и времени.')
        else:
            connect = sqlite3.connect(BD)
            cur = connect.cursor()
            cur.execute('INSERT INTO notes (userid, date, time, notes) '
                        'VALUES (?,?,?,?);', [message.from_user.id, date.timestamp(),
                                              tm.timestamp(), text_str])
            connect.commit()
            cur.execute('SELECT id FROM notes where userid = ? and date = ? '
                        'and time = ? and notes = ? ORDER BY id DESC',
                        [message.from_user.id, date.timestamp(), tm.timestamp(), text_str])
            note_id = cur.fetchone()[0]

            mess = text.add4
            await message.answer(mess, parse_mode="Markdown", reply_markup=kb.keyboard)
            mess = '*' + str(dttm.strftime("%d.%m.%y %H:%M")) + '*'
            mess += '\n' + text_str
            await message.answer(mess, parse_mode="Markdown", reply_markup=kb.edit(note_id))
            logging.info(message.from_user.full_name + ' - добавил новую запись.')
    await state.finish()

