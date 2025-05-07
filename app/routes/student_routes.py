from fastapi import APIRouter, HTTPException
from app.schemas.student_schema import StudentSchema
from app.controllers import student_controller

router = APIRouter()

@router.get("/student/{id}")
async def get_student(id: str):
    student = await student_controller.get_student(id)
    if student:
        return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@router.get("/students")
async def list_students():
    return await student_controller.get_all_students()

@router.post('/students/create')
async def create_student(student: StudentSchema):
    return await student_controller.create_student(student.dict())

@router.delete("/students/{id}/delete")
async def delete_student(id: str):
    status = await student_controller.delete_student(id)
    if not status:
        raise HTTPException(status_code=404, detail="student not found")
    return {
        "message": "student deleted successfully"
    }