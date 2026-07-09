from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "3 Idiots",
        "director": "Rajkumar Hirani",
        "genre": "Comedy Drama",
        "language": "Hindi",
        "release_year": 2009,
    },
    {
        "id": 2,
        "title": "Baahubali",
        "director": "S S Rajamouli",
        "genre": "Action Drama",
        "language": "Telugu",
        "release_year": 2015,
    },
]


@app.get("/")
def greet():
    return {"Message": "Working with movies dataset"}


@app.get("/movies")
def all_movies():
    return movies


@app.get("/movies/{id}")
def get_movie_by_id(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    raise HTTPException(status_code=404, detail="Movie Not Found")


class UpdateMovie(BaseModel):
    title: str
    director: str
    genre: str
    language: str
    release_year: int


@app.put("/movies/{id}")
def update_movie(id: int, movie: UpdateMovie):
    for existing_movie in movies:
        if existing_movie["id"] == id:
            existing_movie.update(movie.model_dump())
            return {"Message": "Updated Successfully", "Movie": existing_movie}
    raise HTTPException(status_code=404, detail="Movie Not Found")


class PatchMovie(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    genre: Optional[str] = None
    language: Optional[str] = None
    release_year: Optional[str] = None


@app.patch("/movies/{id}")
def patch_movie(id: int, movie: PatchMovie):
    for existing_movie in movies:
        if existing_movie["id"] == id:
            # if movie.title is not None:
            #     existing_movie["title"] = movie.title
            # if movie.director is not None:
            #     existing_movie["director"] = movie.director
            # if movie.genre is not None:
            #     existing_movie["genre"] = movie.genre
            # if movie.language is not None:
            #     existing_movie["language"] = movie.language
            # if movie.release_year is not None:
            #     existing_movie["release_year"] = movie.release_year
            existing_movie.update(movie.model_dump(exclude_none=True))
            return {"Message": "Updated Successfully", "Movie": existing_movie}
    raise HTTPException(status_code=404, detail="Movie Not Found")


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"Message": "Deletion successful"}
    raise HTTPException(status_code=404, detail="Movie Not Found")
