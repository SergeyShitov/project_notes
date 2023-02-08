from pydantic import BaseModel
import uuid
import datetime

class Note(BaseModel):
    id = uuid.uuid4()
    title: str
    text: str
    data_time = datetime.datetime.now()

