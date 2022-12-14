"""
Вася решил передать Пете шифрограмму.
Поскольку о промышленных шифрах Вася ничего не знает,
он решил шифровать сообщение следующим образом: он посылает Пете строку.

1) Каждый символ строки - либо буква, либо пробел, либо точка ".", либо две точки "..".
2) если после какой-то буквы стоит точка, значит мы оставляем букву без изменений
    (об 1ой точке Вася задумался чтобы усложнить расшифровку). Саму точку при этом надо удалить
3) если после какой-то буквы стоит две точки, то предыдущий символ надо стереть.
    Обе точки при этом тоже нужно удалить
4) возможна ситуация, когда сообщение после расшифровки будет пустым.
    В качестве результата можно вернуть просто пустую строку

Помогите Пете написать программу для расшифровки.

Примеры шифровок-расшифровок:
абра-кадабра. -> абра-кадабра
абраа..-кадабра -> абра-кадабра
абраа..-.кадабра -> абра-кадабра
абра--..кадабра -> абра-кадабра
абрау...-кадабра -> абра-кадабра (сначала срабатывает правило 2х точек, потом правило 1ой точки)
абра........ -> <пустая строка>
абр......a. -> a
1..2.3 -> 23
. -> <пустая строка>
1....................... -> <пустая строка>

"""


def decrypt(s: str) -> str:
    """
    Func decodes input str. Symbol before '..' is removed, symbol before '.' is not changing. All '.' are removed
    :param s: input str
    :return: decode str
    """
    result = []

    for symbol in s:
        result.append(symbol)
        if len(result) > 2 and (result[-2], result[-1]) == ('.', '.'):
            result.pop(-1)
            result.pop(-1)
            if result:
                result.pop(-1)
    decode_str = ''.join(symbol for symbol in result if symbol != '.')
    return decode_str


if __name__ == "__main__":
    decrypt('абра-кадабра.')
    # decrypt('абраа.. - кадабра')
    # decrypt('абраа.. -.кадабра')
    # decrypt('абра - -..кадабра')
    # decrypt('абрау... - кадабра')
    # decrypt('абра........')
    # decrypt('абр......a.')
    # decrypt('1..2.3')
    # decrypt('.')
    # decrypt('1........')
