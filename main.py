from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import Atleta, Entrenamiento

app = FastAPI(title="API de Entrenamiento Deportivo")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- CRUD ATLETAS ---
@app.post("/atletas/", response_model=Atleta)
def crear_atleta(atleta: Atleta, session: Session = Depends(get_session)):
    session.add(atleta)
    session.commit()
    session.refresh(atleta)
    return atleta

@app.get("/atletas/", response_model=list[Atleta])
def leer_atletas(session: Session = Depends(get_session)):
    atletas = session.exec(select(Atleta)).all()
    return atletas

# --- CRUD ENTRENAMIENTOS ---
@app.post("/entrenamientos/", response_model=Entrenamiento)
def crear_entrenamiento(entrenamiento: Entrenamiento, session: Session = Depends(get_session)):
    session.add(entrenamiento)
    session.commit()
    session.refresh(entrenamiento)
    return entrenamiento

@app.get("/entrenamientos/", response_model=list[Entrenamiento])
def leer_entrenamientos(session: Session = Depends(get_session)):
    entrenamientos = session.exec(select(Entrenamiento)).all()
    return entrenamientos