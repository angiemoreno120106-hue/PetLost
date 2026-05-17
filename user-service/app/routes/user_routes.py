from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


# ======================
# DB DEPENDENCY
# ======================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ======================
# CREATE USER
# ======================
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    try:
        user.validate_all()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email ya existe")

    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ======================
# GET ALL USERS
# ======================
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# ======================
# GET USER BY ID
# ======================
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user


# ======================
# UPDATE USER
# ======================
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        user.validate_all()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    email_exists = db.query(User).filter(
        User.email == user.email,
        User.id != user_id
    ).first()

    if email_exists:
        raise HTTPException(status_code=400, detail="Email ya está en uso")

    db_user.name = user.name
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.password = user.password

    db.commit()
    db.refresh(db_user)

    return db_user


# ======================
# DELETE USER
# ======================
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()

    return {
        "message": "Usuario eliminado correctamente",
        "id": user_id
    }