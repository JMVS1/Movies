from fastapi import FastAPI
 
app = FastAPI(title='Proyecto Individual Juan Manuel Valderrama',
              description='Recomendacion de peliculas Henry Student',
              version='1.0.1')
@app.get('/')
def index():
    return 'Proyecto individual Juan Manuel Valderrama'
 
@app.get('/about')
def about():
    return 'Recomendacion de peliculas Henry Student'


import pandas as pd

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str):
    mes = mes.lower()
    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }

    mes_numero = meses.get(mes)
    if mes_numero is None:
        return {'error': 'Mes inválido'}

    # Cargar el archivo CSV
    df = pd.read_csv('movie_final.csv')

    # Convertir la columna "release_date" a un objeto de tipo fecha
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # Filtrar el DataFrame por el mes especificado
    month_filtered = df[df['release_date'].dt.month == mes_numero]

    # Filtrar valores duplicados del DataFrame y calcular la cantidad de películas
    month_unique = month_filtered.drop_duplicates(subset='id')
    respuesta = month_unique.shape[0]

    return {'mes': mes, 'cantidad de peliculas': respuesta}



import pandas as pd

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    dia = dia.lower()
    dias_semana = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'domingo': 6
    }

    dia_numero = dias_semana.get(dia)
    if dia_numero is None:
        return {'error': 'Día inválido. Por favor, ingrese un día válido en español.'}

    # Cargar el archivo CSV
    df = pd.read_csv('movie_final.csv')

    # Convertir la columna "release_date" a un objeto de tipo fecha
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # Filtrar el DataFrame por el día de la semana especificado
    dia_filtered = df[df['release_date'].dt.dayofweek == dia_numero]

    # Contar la cantidad de filmaciones
    cantidad = dia_filtered.shape[0]

    return {'dia': dia, 'cantidad': cantidad}


import pandas as pd

# Cargar el DataFrame con los datos de películas
df = pd.read_csv("movie_final.csv")  # Reemplaza con la ruta correcta de tu archivo CSV

@app.get("/score/{titulo}")
def score_titulo(titulo: str):
    # Buscar la película por título en el DataFrame
    pelicula = df[df["title"] == titulo]
    
    # Verificar si se encontró una coincidencia
    if len(pelicula) == 0:
        return {"message": "No se encontró la película."}
    
    # Obtener el título, año de estreno y score/popularidad
    titulo = pelicula["title"].values[0]
    estreno = pelicula["release_year"].values[0]
    score = pelicula["popularity"].values[0]
    
    return {
        "message": f"La película {titulo} fue estrenada en el año {estreno} con un score/popularidad de {score}."
    }


import pandas as pd


# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("movie_final.csv")


@app.get("/votos/{titulo_de_la_filmacion}")
def votos_titulo(titulo_de_la_filmacion: str):
    # Buscar la película por el título en el DataFrame
    pelicula = df[df['title'] == titulo_de_la_filmacion]

    if pelicula.empty:
        return {"mensaje": "No se encontró ninguna película con ese título."}

    votos = pelicula['vote_count'].values[0]
    promedio = pelicula['vote_average'].values[0]

    if votos < 2000:
        return {"mensaje": "La película no cumple con el requisito mínimo de 2000 valoraciones."}

    retorno = f"La película {titulo_de_la_filmacion} fue estrenada en el año {pelicula['release_year'].values[0]}."
    retorno += f" La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}."

    return {"retorno": retorno}


import pandas as pd


# Cargar el DataFrame desde el archivo CSV
data = pd.read_csv("actor_final.csv")

@app.get("/actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    # Filtrar las filas que contienen al actor especificado
    actor_films = data[data["name"] == nombre_actor]

    # Excluir las filas donde el actor es un director (si existe la columna "job")
    if "job" in actor_films.columns:
        actor_films = actor_films[actor_films["job"] != "Director"]

    # Obtener la cantidad de películas del actor
    cantidad_films = len(actor_films)

    # Calcular el promedio de retorno del actor
    promedio_retorno = actor_films["return"].mean()

    # Obtener el éxito del actor según el promedio de retorno
    exito = "Bajo"
    if promedio_retorno > 1.0:
        exito = "Alto"
    elif promedio_retorno > 0.5:
        exito = "Moderado"

    return {
        "actor": nombre_actor,
        "cantidad_films": cantidad_films,
        "promedio_retorno": promedio_retorno,
        "exito": exito
    }
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("direct.final.csv")

@app.get("/director/{nombre_director}")
def get_director(nombre_director: str):
    director_movies = df[df["name"] == nombre_director]

    if director_movies.empty:
        return {"error": "No se encontraron datos para el director especificado."}

    director_movies = director_movies[["name", "return", "title", "release_date", "budget", "revenue"]]
    director_movies = director_movies.drop_duplicates(subset="title")

    exito = director_movies["return"].mean()

    peliculas = []
    for _, row in director_movies.iterrows():
        pelicula = {
            "titulo": row["title"],
            "fecha_lanzamiento": row["release_date"],
            "retorno_individual": row["return"],
            "costo": row["budget"],
            "ganancia": row["revenue"],
        }
        peliculas.append(pelicula)

    return {
        "exito": exito,
        "peliculas": peliculas,
    }


from typing import List
import pandas as pd
from sklearn.neighbors import NearestNeighbors


df = pd.read_csv("movie_final.csv")
model = NearestNeighbors(n_neighbors=50)  # Aumentamos el número de vecinos a considerar
model.fit(df[["budget", "vote_average"]])

def recommendation(title):
    if title not in df["title"].values:
        raise KeyError(f"The movie '{title}' is not present in the dataset.")

    title_index = df[df["title"] == title].index[0]
    distances, indices = model.kneighbors([df.loc[title_index, ["budget", "vote_average"]]])

    recommended_titles = []
    i = 0
    while len(recommended_titles) < 5 and i < len(indices[0]):
        index = indices[0, i]
        recommended_title = df.loc[index, "title"]
        if recommended_title != title and recommended_title not in recommended_titles:
            recommended_titles.append(recommended_title)
        i += 1

    if len(recommended_titles) < 5:
        remaining_indices = df.index[~df.index.isin(indices[0])]
        remaining_titles = df.loc[remaining_indices, "title"].sample(n=5 - len(recommended_titles), random_state=42)
        recommended_titles.extend(remaining_titles)

    return recommended_titles

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    try:
        recomendaciones = recommendation(titulo)
        return {'lista recomendada': recomendaciones}
    except KeyError as e:
        return {'error': str(e)}



import pandas as pd


# Cargar el archivo CSV
df = pd.read_csv("direct.final.csv")

@app.get("/director/{nombre_director}")
def get_director(nombre_director: str):
    director_movies = df[df["name"] == nombre_director]

    if director_movies.empty:
        return {"error": "No se encontraron datos para el director especificado."}

    director_movies = director_movies[["name", "return", "title", "release_date", "budget", "revenue"]]
    director_movies = director_movies.drop_duplicates(subset="title")

    exito = director_movies["return"].mean()

    peliculas = []
    for _, row in director_movies.iterrows():
        pelicula = {
            "titulo": row["title"],
            "fecha_lanzamiento": row["release_date"],
            "retorno_individual": row["return"],
            "costo": row["budget"],
            "ganancia": row["revenue"],
        }
        peliculas.append(pelicula)

    return {
        "exito": exito,
        "peliculas": peliculas,
    }


