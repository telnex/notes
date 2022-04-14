from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

# -----------------------------------------------------------
# ReplyKeyboardMarkup
# -----------------------------------------------------------

# Main
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton(text='Старт'))
keyboard.add(KeyboardButton(text='Добавить запись'))

# cancel
cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add(KeyboardButton(text='Отмена'))


# -----------------------------------------------------------
# InlineKeyboardButton
# -----------------------------------------------------------
home = InlineKeyboardMarkup()
home.row(
        InlineKeyboardButton('На сегодня', callback_data='today'),
        InlineKeyboardButton('На завтра', callback_data='tomorrow'),
    )

# Скачать лог
download_log = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Download bot.log', callback_data='download_log')
)

def today(imp: int = 0):
    """ link today.py """
    menu = InlineKeyboardMarkup()
    if imp == 1:
        menu.row(
            InlineKeyboardButton('Только важные', callback_data='imp_today')
        )
    elif imp == 2:
        menu.row(
            InlineKeyboardButton('◉ Только важные', callback_data='imp_today')
        )
    else:
        pass
    menu.row(
        InlineKeyboardButton('◉ На сегодня', callback_data='today'),
        InlineKeyboardButton('На завтра', callback_data='tomorrow'),
        InlineKeyboardButton(u'\U0001F4DD', callback_data='edit_today')
    )
    return menu


def tomorrow(imp: int = 0):
    """ link tomorrow.py """
    menu = InlineKeyboardMarkup()
    if imp == 1:
        menu.row(
            InlineKeyboardButton('Только важные', callback_data='imp_tomorrow')
        )
    elif imp == 2:
        menu.row(
            InlineKeyboardButton('◉ Только важные', callback_data='imp_tomorrow')
        )
    else:
        pass
    menu.add(
        InlineKeyboardButton('На сегодня', callback_data='today'),
        InlineKeyboardButton('◉ На завтра', callback_data='tomorrow'),
        InlineKeyboardButton(u'\U0001F4DD', callback_data='edit_tomorrow')
    )
    return menu


def edit(id: int):
    """ link change.py """
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton(u'\U000026A1', callback_data='imp_' + str(id)),
        InlineKeyboardButton(u'\U0000274C', callback_data='del_' + str(id))
    )
    return kb