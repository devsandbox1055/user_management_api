from sqlalchemy.orm import Session
from app import models
from app import schemas

# yaha pe models.py ka createuser hai uske data ko yaha connect kar rahe hai
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email) # creating python object here
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user