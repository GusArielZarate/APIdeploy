from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Atleta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    especialidad: str  # Ej: "Calistenia", "Running 10k"

    # Relación uno a muchos
    entrenamientos: List["Entrenamiento"] = Relationship(back_populates="atleta")

class Entrenamiento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str  # Ej: "Fondo 5k", "Saco de boxeo"
    duracion_minutos: int
    atleta_id: Optional[int] = Field(default=None, foreign_key="atleta.id")

    # Relación inversa
    atleta: Optional[Atleta] = Relationship(back_populates="entrenamientos")