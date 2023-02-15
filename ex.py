# from pydantic import BaseModel
import uuid
import datetime


class Note:
    id: uuid.UUID
    title: str
    text: str
    data_time: datetime.datetime

    def __init__(self, id, title, text, data_time):
        self.id = id
        self.title = title
        self.text = text
        self.data_time = data_time

    def __str__(self):
        return self.id.__str__() + ' ' + self.title + ' ' + self.text + ' ' + self.data_time.__str__()


class Notes:
    lst: list[Note]

    def __init__(self):
        self.lst = []

    def create_note(self, title, text) -> uuid.UUID:
        id = uuid.uuid4()
        d = datetime.datetime.now()
        note = Note(id, title, text, d)
        self.lst.append(note)
        return id

    def read_note(self, id) -> Note:
        for note in self.lst:
            if note.id == id:
                return note

    def update_note(self, id, text, title) -> uuid.UUID | None:
        for note in self.lst:
            if note.id == id:
                note.title = title
                note.text = text
                return id

    def delete_note(self, id) -> uuid.UUID | None:
        for note in self.lst:
            if note.id == id:
                self.lst.remove(note)
                return id

    def __str__(self):
        representation = ''
        for note in self.lst:
            representation += note.__str__() + '\n'
        return representation


# first = Note(uuid.uuid4(), input(), input(), datetime.datetime.now())
# print('ID: ' + str(first.id), 'Название: ' + first.title, 'Текст: ' + first.text, 'Время создания: ' + str(first.data_time), sep = '\n')


first_notes = Notes() # создание экземпляра класса
first_note_id = first_notes.create_note('Title0', 'Text0')  # создание заметки. возвращаем только ID
first_note_id_1 = first_notes.create_note('Title1', 'Text1')
first_note_id_2 = first_notes.create_note('Title2', 'Text2')


print(first_note_id, end='\n\n')  # выводим только ID

print(first_notes, end='\n')

note_which_was_read = first_notes.read_note(first_note_id) # чтение заметки по выведенному ID
note_which_was_read_1 = first_notes.read_note(first_note_id_1)
note_which_was_read_2 = first_notes.read_note(first_note_id_2)

print(note_which_was_read)
print(note_which_was_read_1)
print(note_which_was_read_2, end='\n\n')

note_which_was_deleted = first_notes.delete_note(first_note_id) # удаление заметки из списка по ID
print(note_which_was_deleted)
print('\n')

note_which_was_edited = first_notes.update_note(first_note_id, 'Text_update', 'Title_update')
note_which_was_edited_1 = first_notes.update_note(first_note_id_1, 'Text_update_1', 'Title_update_1') # обновление заметки (замена названия и текста)
note_which_was_edited_2 = first_notes.update_note(first_note_id_2, 'Text_update_2', 'Title_update_2')

print(note_which_was_edited)
print(note_which_was_edited_1)
print(note_which_was_edited_2, end='\n\n')

print(first_notes)