from fastapi import APIRouter, HTTPException
from app.schemas.student_schema import StudentSchema
from app.controllers import student_controller
from bson import ObjectId

router = APIRouter()

@router.get("/student/{id}")
async def get_student(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=500, detail="invalid object id format")
        return await student_controller.get_student(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/students", response_description="List all students")
async def list_students():
    try:
        return await student_controller.get_all_students()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/student/create')
async def create_student(student: StudentSchema):
    try:
        return await student_controller.create_student(student.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/student/{id}/delete")
async def delete_student(id: str):
    try:
        response = await student_controller.delete_student(id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/student/{id}/update")
async def update_student(id: str, student: StudentSchema):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=500, detail="Invalid object id")
        return await student_controller.update_student(id, student.dict())    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))