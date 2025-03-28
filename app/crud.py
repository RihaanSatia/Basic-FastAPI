from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from datetime import timezone

def createExpense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(amount=expense.amount, 
                                type=expense.type,
                                category = expense.category,
                                description=expense.description,
                                timestamp=datetime.now(timezone.utc))
    
    
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def getExpenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Expense).offset(skip).limit(limit).all()
