import json


def load_data(patch):
    """
    Функция для чтения json файла
    """
    with open(patch, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def filter_sort(data):
    """
    Функция для сортировки данных по дате при условии выполнения операции(EXECUTED)
    """
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data


def formatted_data(item):
    """
    Функция для вывода данных в нужном формате
    """
    item_date = format_date(item.get('date'))

    item.get('from')
    if item.get('from'):
        from_ = mask_card(item.get('from')) + '->'
    else:
        from_ = ''

    to_ = mask_card(item.get('to'))

    return f"{item_date} {item.get('description')}\n" \
           f"{from_}{to_}\n" \
           f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n"


def format_date(str_date):
    """
    Функция для форматирования вводных данных о дате
    """
    list_date = str_date[0:10].split('-')
    return '.'.join(reversed(list_date))


def mask_card(card):
    """
    Функция для маскировки номера карты и номера счета
    """
    card = card.split(' ')
    if card[0] == "Счет":
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])} {card[-1][: 4]} {card[-1][4: 6]}** **** {card[-1][-4:]}'
