from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    name: str
    age: int
    grade: str

students = [
    Student(name="Alice", age=20, grade="A"),
    Student(name="Bob", age=22, grade="B"),
]

@app.get("/students/")
def get_students():
    return students

@app.post("/students/")
def add_student(student: Student):
    students.append(student)
    return student

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if 0 <= student_id < len(students):
        return students[student_id]
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if 0 <= student_id < len(students):
        del students[student_id]
        return {"message": "Student deleted"}
    return {"error": "Student not found"}