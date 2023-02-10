#from pydantic import BaseModel
import uuid
import datetime

class Note:
    id: str
    title: str
    text: str
    data_time = str

    def __init__(self, id, title, text, data_time):
        self.id = id
        self.title = title
        self.text = text
        self.data_time = data_time


first = Note(uuid.uuid4(), input(), input(), datetime.datetime.now())
print(first.__dict__)
print(first.id, first.title, first.text, first.data_time)