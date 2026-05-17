from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, name: str, email: str, password: str, phone: str):
    user = User(name=name, email=email, password=password, phone=phone)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user