from app.database.mongodb import db
from app.models.student_model import student_helper
from bson import ObjectId
from fastapi.responses import JSONResponse

collection = db.students

async def get_student(id: str):
    try:
        student = await collection.find_one({"_id": ObjectId(id)})
        if not student:
            response = {"status": False, "message": f"student with ID {id} is not found"}
    except Exception as e:
        response = {"status": False, "message": f"Error: {str(e)}"}
        return JSONResponse(status_code=500, content=response)
        
        
async def get_all_students():
    try:
        students = []
        async for student in collection.find():
            students.append(student_helper(student))
        response = {"status": True, "data": students}
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response = {"message": f"Error: {e}", "status": False}
        return JSONResponse(status_code=500, content=response)

async def create_student(data: dict) -> dict:
    student = await collection.insert_one(data)
    new_student = await collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

async def delete_student(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0

