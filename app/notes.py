from sqlalchemy.orm import Session
from app import models , schemas

def create_note(note:schemas.NoteCreate, db:Session, user):
    new_note=models.Note(
        title=note.title,
        description=note.description,
        user_id=user.id
    
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

def get_user_notes(db: Session, user):
    return db.query(models.Note).filter(models.Note.user_id == user.id).all()

