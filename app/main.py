from fastapi import FastAPI , Depends , HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from app.database import Base , engine , get_db
from app import models , schemas , notes
from app.auth import hash_password , verify_password , create_access_token , get_current_user


app = FastAPI(title="CloudNotes API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message":"CloudNotes API is running!"}


@app.post("/register")
def register(user:schemas.UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code = 400 , detail="Email alreday registered")
    
    new_user=models.User(email=user.email, password=hash_password(user.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User registered successfully!"}

@app.post("/login")
def login(user:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.username).first()
    if not existing_user or not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401,detail="Invalid email or password")
    
    access_token=create_access_token(data={"sub":existing_user.email})

    return {"access_token":access_token, "token_type":"bearer"}


@app.post("/notes")
def add_note(note:schemas.NoteCreate, 
             db:Session = Depends(get_db),
             user=Depends(get_current_user)
            ):
            return notes.create_note(note, db ,user)

@app.get("/notes",response_model=list[schemas.NoteResponse])
def read_notes(
      db:Session =Depends(get_db),
      user=Depends(get_current_user)
):
     return notes.get_user_notes(db, user)
