##  Sistema de Recomendación de Películas
El objetivo de este proyecto es desarrollar un sistema de recomendación de películas. Se nos han proporcionado dos conjuntos de datos en formato CSV: "movies_dataset" y "credits_dataset". Estos conjuntos de datos se utilizarán para realizar el ETL correspondiente y obtener la información necesaria para el sistema de recomendación.

## ETL del conjunto de datos "movies_dataset"
El conjunto de datos "movies_dataset" ha sido sometido a un proceso de ETL para prepararlo antes de utilizarlo en el sistema de recomendación. A continuación se detallan las transformaciones realizadas:

Desanidación de columnas: Se han desanidado algunas columnas en el conjunto de datos, como "genres" y "production_companies", para facilitar el acceso a la información contenida en ellas.

Manejo de valores nulos: Los valores nulos de los campos "revenue" y "budget" se han reemplazado por el número 0.

Eliminación de valores nulos: Se han eliminado las filas que contienen valores nulos en el campo "release_date".

Formato de fechas: Se ha asegurado que las fechas en el campo "release_date" sigan el formato AAAA-mm-dd. Además, se ha creado la columna "release_year" para extraer el año de la fecha de estreno.

Cálculo del retorno de inversión: Se ha creado la columna "return" que representa el retorno de inversión, calculado dividiendo los campos "revenue" y "budget". En casos donde no hay datos disponibles para calcularlo, se asigna el valor 0.

Eliminación de columnas no utilizadas: Se han eliminado las columnas "video", "imdb_id", "adult", "original_title", "poster_path" y "homepage", ya que no serán utilizadas en el sistema de recomendación.

Con estas transformaciones, se obtiene un conjunto de datos "movies_final" listo para ser utilizado en el sistema de recomendación.

ETL del conjunto de datos "credits_dataset"
El conjunto de datos "credits_dataset" también requiere un proceso de ETL para complementar la información necesaria en el sistema de recomendación. A continuación se detallan las transformaciones realizadas:

Desanidación de columnas: El conjunto de datos contiene las columnas "cast" y "crew" que requieren desanidación para acceder a la información detallada de actores y directores.

Creación de dataframes: Se han creado dos dataframes, "cast_data" y "crew_data", a partir de las columnas desanidadas. Estos dataframes se utilizarán para las consultas de las funciones de actor y director.

Unión con el dataframe principal: El dataframe "cast_data" y crew_data se ha unido con el dataframe principal "movies_final" utilizando un identificador único para cada película. Esto permite obtener la información de actores junto con los demás datos relevantes.

Eliminación de columnas no utilizadas: Se han eliminado las columnas innecesarias en los dataframes "cast_data" y "crew_data" que no serán utilizadas en las consultas.

Finalmente, se han creado dos archivos CSV finales para las consultas de la función de actor y la función de director, que contienen la información necesaria para realizar las recomendaciones correspondientes.

## Análisis Exploratorio de Datos (EDA)
Se ha realizado un análisis exploratorio de datos utilizando el conjunto de datos "movies_final" con el fin de obtener información relevante y visualizar patrones en los datos. A continuación, se presentan algunas de las observaciones destacadas:

Se ha utilizado el método info() y describe() para analizar las columnas numéricas y obtener estadísticas descriptivas.

Se han creado gráficos de dispersión y histogramas para visualizar las distribuciones y relaciones entre las variables.

Se ha generado una "nube de palabras" a partir de los títulos de las películas. Esta nube de palabras muestra las palabras más frecuentes en los títulos en un tamaño mayor y de manera visualmente atractiva.

En el análisis exploratorio de datos, se han identificado algunos aspectos destacados, como la presencia de outliers en varias columnas y la existencia de valores faltantes en la columna "runtime".

## Modelo de Machine Learning
El sistema de recomendación de películas se basa en un modelo de machine learning utilizando el algoritmo de vecinos más cercanos (Nearest Neighbors) de la biblioteca scikit-learn. El modelo busca películas similares en función de las características de presupuesto (budget) y calificación promedio de votos (vote_average).

El modelo de vecinos más cercanos es adecuado para un sistema de recomendación de películas, ya que busca películas similares en función de su proximidad en el espacio de características. En este caso, el espacio de características está definido por el presupuesto y la calificación promedio de votos. Al considerar estas dos características, el modelo puede encontrar películas que son financieramente similares y tienen una calificación promedio similar.

El modelo toma como entrada el título de una película y devuelve una lista de recomendaciones de películas similares. Calcula la distancia entre las características de la película de entrada y las demás películas en el conjunto de datos. Luego, selecciona las películas más cercanas en función de su distancia y las devuelve como recomendaciones.

## API
Se ha desarrollado una API utilizando el framework FastAPI para el sistema de recomendación de películas. La API proporciona las siguientes funciones para realizar consultas:

Consulta de películas por actor: Permite obtener las películas en las que ha participado un actor específico.

Consulta de películas por director: Permite obtener las películas dirigidas por un director específico.

La API se ha desplegado en Render, y se puede acceder a ella a través del siguiente enlace: https://movies-or65.onrender.com/docs

## Documentación adicional
Para obtener más información detallada sobre la configuración y ejecución del proyecto, así como instrucciones para la instalación de las dependencias necesarias, consulte el archivo README.md en el repositorio correspondiente.

## Demostración
Se ha creado un video de presentación que muestra una demostración del sistema de recomendación de películas en funcionamiento. El video destaca las características clave del sistema y muestra los resultados obtenidos. Puedes ver la demostración en el siguiente enlace: https://www.loom.com/share/8e1ff25ed8b44c8ba86cdae56638c9ff?sid=864255e6-9e2f-4a0e-8549-223dd32e499b


## Observaciones
En la consulta en la que retorna un dia y da el numero de peliculas en ese dia el miércoles y sábado llevan tilde. 