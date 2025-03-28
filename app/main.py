from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import os
print("DB Path:", os.path.abspath("expenses.db"))


@app.get("/")
def root():
    return {"message": "Welcome to the expense tracker API!"}

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: SessionLocal = Depends(get_db)):
    return crud.createExpense(db=db, expense=expense)

@app.get("/expenses/", response_model=list[schemas.Expense])
def read_expense(db: Session = Depends(get_db)):
    return crud.getExpenses(db=db)

