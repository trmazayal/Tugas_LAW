import uuid

from models import Note
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

@app.get('/notes/{user_name}',tags=["Notes"])
def Notes(user_name: str):
    notes = db.GetNotes(user_name)
    ret = [
        {x:y for (x,y) in zip(DB_COLLUMN, row)}
        for row in notes
    ]
    return ret

@app.get('/note_id/{note_id}', tags=["Notes"])
def GetNote(note_id: str):
    note = db.GetNoteByID(note_id)
    ret = {x:y for (x,y) in zip(DB_COLLUMN, note)}
    return ret

@app.post('/add_note', tags=["Notes"])
def AddNote(note: Note):
    note.note_id = str(uuid.uuid4())
    db.AddNote(note)
    return note

@app.delete('/delete_note/{note_id}', tags=["Notes"])
def DeleteNote(note_id: str):
    db.DeleteNote(note_id)
    return {"note_id": note_id}

@app.put('/update_note/{note_id}', response_model=Note, tags=["Notes"])
def UpdateNote(note: Note):
    db.UpdateNote(note)
    return note

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    context = {"message": f"{base_error_message}. Detail: {err}"}
    return JSONResponse(status_code=400,content=context)
