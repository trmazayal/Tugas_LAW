import os, time
import psycopg2

def CreateTable():
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS notes(
        note_id varchar(64) NOT NULL,
        title varchar(128) NOT NULL,
        date varchar(64) NOT NULL,
        text varchar(1024) NOT NULL,
        username varchar(128) NOT NULL,
        color varchar(8) NOT NULL,
        PRIMARY KEY (note_id)); ''')
    
    connection.commit()

while True:
    try:
        connection = psycopg2.connect(
            host = os.environ['DB_HOST'],
            database = os.environ['DB_NAME'],
            user = os.environ['DB_USERNAME'],
            password = os.environ['DB_PASSWORD']
        )
        cursor = connection.cursor()
        print("Connected to database")
        break
        
    except Exception as error:
        print("Connecting to database failed..., retrying in 2 seconds")
        print("Error:", error)
        time.sleep(2)
        
def GetNotes(username):
    cursor.execute(f'''SELECT * from notes WHERE username='{username}';''')
    return cursor.fetchall()

def GetNoteByID(note_id):
    cursor.execute(f'''SELECT * from notes WHERE note_id='{note_id}';''')
    return cursor.fetchone()

def AddNote(note):
    values = (note.note_id, note.title, note.date, 
                note.text, note.username, note.color)
    cursor.execute(f'''INSERT INTO notes(note_id, title, date, text, username, color)
    VALUES(%s, %s, %s, %s, %s, %s);''', values)
    connection.commit()    

def DeleteNote(note_id):
    cursor.execute(f'''DELETE FROM notes WHERE note_id='{note_id}';''')
    connection.commit()

def UpdateNote(note):
    values = (note.title, note.date, note.text, note.color, note.note_id)
    cursor.execute(f'''UPDATE notes SET title=%s, date=%s, text=%s, color=%s WHERE note_id=%s;''', values)
    connection.commit()
