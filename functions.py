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