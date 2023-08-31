from utils import load_data, formatted_data, filter_sort

JSON_FILE = 'operations.json'


def main():
    """
    Функция выводит 5 последних операций
    """
    data = load_data(JSON_FILE)
    data = filter_sort(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
