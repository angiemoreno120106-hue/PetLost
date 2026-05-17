from pydantic import BaseModel, EmailStr, Field
import re

# =========================
# CREATE USER
# =========================
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone: str | None = None
    password: str = Field(min_length=8)

    def validate_all(self):
        password = self.password

        # 🔐 PASSWORD VALIDATION
        if len(password) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")

        if not any(c.isupper() for c in password):
            raise ValueError("Debe tener al menos una mayúscula")

        if not any(c.isdigit() for c in password):
            raise ValueError("Debe tener al menos un número")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Debe tener al menos un carácter especial")

        # 📱 PHONE VALIDATION (si existe)
        if self.phone:
            if not re.fullmatch(r"\+?[0-9]{7,15}", self.phone):
                raise ValueError("Número de teléfono inválido")

        return password


# =========================
# RESPONSE (SEGURA)
# =========================
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None

    class Config:
        from_attributes = True