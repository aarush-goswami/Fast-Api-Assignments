from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return {"message": "Welcome to my first FastAPI assignment"}


@app.get("/about")
def about():
    return {
        "student_name": "Your Name",
        "course": "FastAPI",
        "topic": "First API Assignment",
        "status": "Learning",
    }


@app.get("/trainer")
def trainer():
    return {"name": "Hemanth", "role": "Trainer"}



@app.get("/courses")
def courses() -> list[Any]:
    return [
        {"id": 1, "name": "Python Basics", "duration": "1 week"},
        {"id": 2, "name": "FastAPI", "duration": "2 weeks"},
        {"id": 3, "name": "SQL Basics", "duration": "1 week"},
    ]


@app.get("/students")
def students() -> list[Any]:
    return [
        {"id": 1, "name": "Akhil", "course": "Python", "city": "Hyderabad"},
        {"id": 2, "name": "Sai", "course": "FastAPI", "city": "Vijayawada"},
    ]


@app.get("/college")
def college():
    return {
        "college_name": "MIET",
        "location": "Jammu",
        "department": "Computer Science",
        "current_module": "FastAPI Basics",
    }


@app.get("/technologies")
def technologies() -> list[str]:
    return ["Python", "FastAPI", "JSON", "HTTP", "REST API"]

@app.get('/students/{student_id}')
def students_by_id(student_id:int) -> dict[str , Any]:
    return {
        "student_id" : student_id,
        "message" : "Learning Dynamic URL's"
    }
    
@app.get('/courses/{course_name}')
def course_by_id(course_name:str):
    return {
        "course_name" : course_name,
        "message" : "Course for learning Dynamic URL's"
    }
@app.get('/books/{book_id}/author/{author_id}')
def book_and_author_by_id(book_id : int,author_id : int)->dict[str,int|Any]:
    return {
        "book name" : "MAjh",
        "book_id" : book_id,
        "author_name" : "Premchand",
        "author_id" : author_id
    }
@app.get('/students/{student_id}/courses/{course_name}')
def student_id_course_name(student_id : int,course_name : str)->dict[str,int|Any]:
    return {
        "student_name" : "Xavier",
        "student_id" : student_id,
        "course" : "Dynamic url",
        "course name" : course_name
    }