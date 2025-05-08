from app.database.mongodb import db
from app.models.student_model import student_helper
from bson import ObjectId
from fastapi.responses import JSONResponse
from app.models.student_model import student_helper


collection = db.students

async def get_student(id: str):
    try:
        student = await collection.find_one({"_id": ObjectId(id)})
        if not student:
            response = {"status": False, "message": f"student with ID {id} is not found"}
            return JSONResponse(status_code=404, content=response)
        response = {"status": True, "data": student_helper(student)}
        return JSONResponse(status_code=200, content=response)        
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
    try:
        student = await collection.insert_one(data)
        new_student = await collection.find_one({"_id": student.inserted_id})
        response = {"status": True, "data": student_helper(new_student)}
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response = {"message": f"Error: {e}", "status": False}
        return JSONResponse(status_code=500, content=response)

async def delete_student(id: str):
    try:
        result = await collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count <= 0:
            response = {"status": False, "message": f"student with ID {id} not found"}
            return JSONResponse(status_code=404, content=response)
        response = {"status": True, "message": f"student with ID {id} deleted successfully"}
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response = {"message": f"Error: {str(e)}", "status": False}
        return JSONResponse(status_code=500, content=response)


async def update_student(id: str, data: dict) -> dict:
    try:
        update_result = await collection.update_one({"_id": ObjectId(id)}, {"$set": data})      
        if update_result.modified_count <= 0:
            response = {"status": False, "message": f"failed to update: {update_result.modified_count}"}
            return JSONResponse(status_code=500, content=response)
        updated_student = await collection.find_one({"_id": ObjectId(id)})
        response = {"status": True, "message": "update successfully", "data": student_helper(updated_student)}
        return JSONResponse(status_code=200, content=response)     
    except Exception as e:
        response = {"message": f"Error: {str(e)}", "status": False}
        return JSONResponse(status_code=500,  content=response)        
