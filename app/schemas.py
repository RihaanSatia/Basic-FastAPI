from pydantic import BaseModel
from datetime import datetime

class ExpenseBase(BaseModel):
    amount: float
    type: str
    category: str
    description: str | None = None

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
