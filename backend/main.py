import uuid

from schemas import Note
import database as db

from fastapi import FastAPI

app = FastAPI()

db.CreateTable()
DB_COLLUMN = [
    'note_id', 'title', 'date', 
    'text', 'username', 'color'
]

@app.get('/')
def Home():
    return "Service is Running..."

@app.get('/notes/{user_name}')
def Notes(user_name: str):
    notes = db.GetNotes(user_name)
    ret = [
        {x:y for (x,y) in zip(DB_COLLUMN, row)}
        for row in notes
    ]
    return ret

@app.get('/note_id/{note_id}')
def GetNote(note_id: str):
    note = db.GetNoteByID(note_id)
    ret = {x:y for (x,y) in zip(DB_COLLUMN, note)}
    return ret

@app.post('/add_note')
def AddNote(note: Note):
    note.note_id = str(uuid.uuid4())
    db.AddNote(note)
    return note

@app.delete('/delete_note/{note_id}')
def DeleteNote(note_id: str):
    db.DeleteNote(note_id)
    return {"note_id": note_id}

@app.post('/update_note')
def UpdateNote(note: Note):
    db.UpdateNote(note)
    return note
