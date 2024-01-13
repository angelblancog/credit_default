# **Práctica Credit Default**

**Autor**: Ángel Blanco García.  
**Institución**: CUNEF Universidad.  
**Programa**: Máster Universitario en Ciencia de Datos.  

### **Datos de contacto**
[<font color='orange'>Correo</font>](angel.blanco@cunef.edu)  
[<font color='lime'>Github</font>](https://github.com/angelblancog/credit_default)  
[Docker](https://hub.docker.com/u/angelbg34)

Este proyecto trata todos los pasos necesarios para la formulación de un modelo de Machine Learning de clasificación sobre un dataset de fraude bancario. que son los siguientes:

1. Definición del problema a resolver y recopilación de datos.

2. Exploración inicial de las variables.

3. Separación en train y test.

4. Tratamiento de missings, outliers y correlaciones.

5. Codificación de las variables categóricas y escalado de los datos.

6. Selección de variables input del modelo.

7. Formulación de un modelo base y prueba de modelos sin ajustar hiperparámetros.

8. Elección del modelo óptimo y ajuste de sus hiperparámetros.

9. Análisis de métricas del modelo.

10. Análisis de explicabilidad.

La idea es hacer modelo sobre datos que tenemos para poder predecir con nuevos datos si la probabilidad de fraude es alta o no.


### **Estructura de carpetas:**

- [data/](data) con subcarpetas preprocessed para datos preprocesados, processed para datos finales y raw para el conjunto de datos vírgenes.

- [docs/](docs) contiene un markdown del diccionario de datos con algo de diseño e información extra, además de las **instrucciones para usar el dashboard**.

- [docker/](docker) con los archivos necesarios para que funcionen las imágenes de server y dashboard para la demo de producción.

- [html/](html) con los html de los notebooks usados.

- [images/](images) con las imágenes utilizadas.

- [metadata/](metadata) con archivo json para mejorar la limpieza y facilitar la lectura del código. 

- [models/](models) que almacena los modelos que se han guardado en pickle.

- [notebooks/](notebooks) con los notebooks de los análisis.

- [references/](references) con el diccionario de datos en pdf.

- [reports/](reports) esta carpeta contiene un markdown de conclusiones de interés.

- [src/](src) donde se han guardado las funciones creadas para el trabajo. La estructura de los archivos py es la siguiente:

   - [_init.py/](src/__init__.py) archivo para que funcionen los imports de las otras funciones.

   - [analysis.py/](src/analysis.py) para funciones relacionadas con el análisis de datos.

   - [const.py/](src/const.py) para simplificar los paths.

   - [data_processing.py/](src/data_processing.py) con funciones para el procesamiento de datos.

   - [data.py/](src/data.py) que contiene funciones para simpificar la lectura y guardado de datos.

   - [metrics.py/](src/metrics.py) funciones para obtener las métricas de los modelos.

   - [models.py/](src/models.py) que simplifica la carga y el guardado de los modelos en pickle.

   - [plots.py/](src/plots.py) funciones de gráficos.
   
   - [prediction.py/](src/prediction.py) funciones para que la app haga predicciones sobre los datos nuevos preprocesados.
   
   - [style.py/](src/style.py) funciones de mejora visual de la API.

   - [types.py/](src/types.py) simplemente con un diccionario con los tipos de variables para el json.


- [tables/](tables) que guarda la tabla de métricas en csv.
