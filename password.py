import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(i.isdigit() for i in password)


def has_letters(password):
    return any(i.isalpha() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/~"
    return any(i in symbols for i in password)


def score_password(password):
    functions = [is_very_long, has_digit, has_letters,
                 has_upper_letters, has_lower_letters, has_symbols]

    score = 0
    for i in functions:
        if i(password):
            score += 2
    return score


def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг пароля: %s" % score_password(new_edit_text))


ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
