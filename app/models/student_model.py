from bson import ObjectId

def student_helper(student) -> dict:
    return {
        "id": str(student["__id"]),
        "name": student["name"],
        "age": student["age"],
        "course": student["course"]
    }

