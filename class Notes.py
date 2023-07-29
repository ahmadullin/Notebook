class Notes:
    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def save_to_json(self, filename):
        data = []
        for note in self.notes:
            data.append({'title': note.title, 'text': note.text, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')})
        with open(filename, 'w') as file:
            json.dump(data, file)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['title', 'text', 'date'])
            for note in self.notes:
                writer.writerow([note.title, note.text, note.date.strftime('%Y-%m-%d %H:%M:%S')])

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        for note_data in data:
            title = note_data['title']
            text = note_data['text']
            date = datetime.strptime(note_data['date'], '%Y-%m-%d %H:%M:%S')
            self.add(Note(title, text, date))

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