#!/usr/bin/env python3
#
# A library that allows to create an inline calendar keyboard.
# grcanosa https://github.com/grcanosa
#

from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove




def create_options_keyboard(options):
    """
    Create an options keyboard with one line featuring each option
    """
    row = []
    for i,op in enumerate(options,cancel_msg):
        row.append(InlineKeyboardButton(op),callback_data="CHOSEN;str(i)")
    row.append(InlineKeyboardButton(cancel_msg),callback_data="CANCEL;0")
    return InlineKeyboardMarkup([row])


def process_option_selection(bot,update):
    data = update.callback_query.data
    action, index = data.split(";")
    if action == "CHOSEN":
        bot.edit_message_text(text=query.message.text,
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            )
        ret_data = True,int(index)
    elif action == "CANCEL":
        bot.edit_message_text(text=query.message.text,
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
            )
        ret_data = False,0
    else:
        bot.answer_callback_query(callback_query_id= query.id,text="Something went wrong!")