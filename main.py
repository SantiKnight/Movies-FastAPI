from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "My FastAPI app"
#app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    overview: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    category: Optional[str] = None

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Fantasia'    
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    return next((item for item in movies if item['id'] == id), [])

@app.get('/movies/', tags=['movies'])
def get_movie_by_category(category):
    return [item for item in movies if item['category'] == category]

@app.post('/movies' , tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = movie.title
            movie['overview'] = movie.overview
            movie['year'] = movie.year
            movie['rating'] = movie.rating
            movie['category'] = movie.category
            return movies
        
@app.delete('/movies', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)      
    return movies