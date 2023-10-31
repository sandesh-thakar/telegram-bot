from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from database import get_database
from models import MessageDB
from schemas import MessageCreate
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/messages/")
async def create_message(message: MessageCreate, db: Session = Depends(get_database)):
    db_message = MessageDB(**message.model_dump())
    db.add(db_message)
    print("here")
    db.commit()
    db.refresh(db_message)
    return db_message


@app.get("/messages/")
async def read_messages(
    limit: int = Query(
        default=10, description="Number of messages to retrieve", ge=1, le=100
    ),
    offset: int = Query(default=0, description="Offset for paginating messages", ge=0),
    db: Session = Depends(get_database),
):
    messages = db.query(MessageDB).offset(offset).limit(limit).all()
    return messages
