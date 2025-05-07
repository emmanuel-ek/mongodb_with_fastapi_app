from pydantic import BaseModel, Field
from typing import Optional

class StudentSchema(BaseModel):
    name: str
    age: int
    course: str