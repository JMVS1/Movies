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

