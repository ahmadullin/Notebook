import json
import csv
from datetime import datetime

class Note:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

class Notes:
    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['title', 'text', 'date'])
            for note in self.notes:
                writer.writerow([note.title, note.text, note.date.strftime('%Y-%m-%d %H:%M:%S')])

    def load_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader) # skip header
            for row in reader:
                title = row[0]
                text = row[1]
                date = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                self.add(Note(title, text, date))

    def filter_by_date(self, date):
        filtered_notes = []
        for note in self.notes:
            if note.date.date() == date.date():
                filtered_notes.append(note)
        return filtered_notes

    def edit(self, index, title=None, text=None):
        note = self.notes[index]
        if title:
            note.title = title
        if text:
            note.text = text

    def delete(self, index):
        del self.notes[index]

# функции для работы с консолью
def print_notes(notes):
    for i, note in enumerate(notes):
        print(f'{i+1}. {note.title} ({note.date.strftime("%Y-%m-%d %H:%M:%S")})')
        print(note.text)
        print()

def add_note():
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    date_str = input('Введите дату и время в формате YYYY-MM-DD HH:MM:SS (нажмите Enter для текущей даты и времени): ')
    if date_str:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    else:
        date = datetime.now()
    notes.add(Note(title, text, date))
    print('Заметка добавлена.')

def edit_note():
    index = int(input('Введите номер заметки для редактирования: ')) - 1
    note = notes.notes[index]
    print(f'Редактирование заметки "{note.title}":')
    new_title = input(f'Введите новый заголовок (нажмите Enter для сохранения текущего: "{note.title}"): ')
    new_text = input(f'Введите новый текст (нажмите Enter для сохранения текущего: "{note.text}"): ')
    notes.edit(index, title=new_title, text=new_text)
    print('Заметка отредактирована.')

def delete_note():
    index = int(input('Введите номер заметки для удаления: ')) - 1
    note = notes.notes[index]
    print(f'Удаление заметки "{note.title}"...')
    notes.delete(index)
    print('Заметка удалена.')

def filter_notes():
    date_str = input('Введите дату для фильтрации в формате YYYY-MM-DD: ')
    date = datetime.strptime(date_str, '%Y-%m-%d')
    filtered_notes = notes.filter_by_date(date)
    if filtered_notes:
        print(f'Заметки за {date_str}:')
        print_notes(filtered_notes)
    else:
        print(f'Нет заметок за {date_str}.')

# основной код
notes = Notes()

while True:
    print('Меню:')
    print('1. Просмотреть все заметки')
    print('2. Добавить новую заметку')
    print('3. Редактировать заметку')
    print('4. Удалить заметку')
    print('5. Фильтровать заметки по дате')
    print('6. Сохранить заметки в файл')
    print('7. Загрузить заметки из файла')
    print('8. Выйти')
    choice = input('Введите номер действия: ')

    if choice == '1':
        print_notes(notes.notes)
    elif choice == '2':
        add_note()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        filter_notes()
    elif choice == '6':
        filename = input('Введите имя файла для сохранения (нажмите Enter для сохранения в notes.json): ')
        if not filename:
            filename = 'notes.json'
        notes.save_to_json(filename)
        print(f'Заметки сохранены в файл "{filename}".')
    elif choice == '7':
        filename = input('Введите имя файла для загрузки (нажмите Enter для загрузки из notes.json): ')
        if not filename:
            filename = 'notes.json'
        notes.load_from_json(filename)
        print(f'Заметки загружены из файла "{filename}".')
    elif choice == '8':
        break
    else:
        print('Неверный выбор, попробуйте еще раз.')
