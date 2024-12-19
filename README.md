CAF-CCH 1950-2024

#### Análisis de factores que incrementan el aumento en el consumo de combustible y la huella de carbono y comparativa entre los 5 países industrializados con más contaminantes (China, India, Estados Unidos, Japón y Rusia) y los 5 países no industrializados con más contaminantes (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) entre 1950 y 2023

El aumento en el consumo de combustibles fósiles y las emisiones de CO₂ son factores clave en el cambio climático. Entre 1950 y 2023, los países industrializados (China, India, Estados Unidos, Japón y Rusia) han liderado las emisiones globales debido a su alto desarrollo industrial. Por otro lado, países no industrializados (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) enfrentan sus propios retos, como el crecimiento poblacional.

El proyecto compara las emisiones y los patrones de contaminación entre ambos grupos, visualizando los datos históricos mediante gráficas generadas en Python para entender mejor las dinámicas y su impacto ambiental.

## Tabla de contenidos

1. [Nombre](#Nombre)
  
2. [Descripción](#descripción)
  
3. [Arquitectura](#Arquitectura)
  
4. [Proceso](#Proceso)
  
5. [Funcionalidades](#Funcionalidades extra)
  
6. [Estado del proyecto](#EstadoDelProyecto)
  
7. [Agradecimientos](#Agradecimientos)
  

# Nombre

Análisis de factores que incrementan el aumento en el consumo de combustible y la huella de carbono y comparativa entre los 5 países industrializados con más contaminantes (China, India, Estados Unidos, Japón y Rusia) y los 5 países no industrializados con más contaminantes (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) entre 1950 y 2023

# Descripcion

Este proyecto analiza los factores que han incrementado el consumo de combustible y la huella de carbono entre 1950 y 2023, comparando las emisiones de CO₂ y otros gases de efecto invernadero entre los cinco países industrializados con mayores emisiones contaminantes (China, India, Estados Unidos, Japón y Rusia) y los cinco países no industrializados con mayores emisiones contaminantes (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía). Utilizando datos históricos y visualizaciones gráficas generadas en Python, el estudio destaca las diferencias en los niveles de emisión y los factores que impulsan estas emisiones en ambos grupos de países, proporcionando conclusiones y recomendaciones para mitigar el impacto ambiental global.

![image](https://github.com/user-attachments/assets/352dee11-630f-4782-bbf3-62666a922eda)

# Arquitectura

El proyecto se organiza en un flujo que comienza con la recopilación de datos históricos sobre emisiones de carbono de la plataforma **Our World in Data**, seguidos por una etapa de limpieza y estructuración de los datos utilizando **Pandas** para asegurar su calidad. Posteriormente, los datos son analizados y visualizados mediante gráficos creados con **Matplotlib** y **Seaborn**, permitiendo identificar tendencias y comparaciones clave. Finalmente, los resultados se integran en una aplicación interactiva desarrollada con **Flet**, donde los usuarios pueden explorar los análisis y personalizar la visualización de forma sencilla e intuitiva.

# Proceso de desarrollo

- Fuente del dataset: [CO₂ and Greenhouse Gas Emissions - Our World in Data](https://ourworldindata.org/co2-and-greenhouse-gas-emissions#explore-data-on-co2-and-greenhouse-gas-emissions)
  
- Limpieza de datos: La limpieza de datos en el código se realizó en varios pasos:
  
  1. **Importación del DataFrame**: Se cargó un archivo CSV que contenía datos relacionados con emisiones de CO2 y otros indicadores.
  2. **Filtrado de Países**: Se filtraron los datos para incluir solo ciertos países específicos (China, India, Estados Unidos, Japón, Rusia, Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía). Esto se hizo utilizando el código ISO de cada país.
  3. **Filtrado de Fechas**: Se filtraron los datos para incluir solo los años entre 1950 y 2023. Esto aseguró que solo se analizaran los datos dentro de este rango de tiempo.
  4. **Eliminación de Columnas**: Se eliminaron varias columnas que no eran necesarias para el análisis. Esto ayudó a simplificar el DataFrame y a enfocarse solo en las columnas relevantes.
  5. **Llenado de Valores Nulos**: Se reemplazaron los valores nulos en el DataFrame con ceros. Esto fue importante para evitar problemas en el análisis y en la generación de gráficos.

![image](https://github.com/user-attachments/assets/42497f3e-4a83-4300-849b-5b08890ff6d7)


- Gráficos
  
  1. Gráfico de toneladas de CO2 a lo largo del tiempo para varios países (China, India, Estados Unidos, Japón, Rusia, Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía).
    
  2. Gráfico de toneladas de CO2 a lo largo del tiempo para países industrializados (China, India, Estados Unidos, Japón y Rusia).
    
  3. Gráfico de toneladas de CO2 a lo largo del tiempo para países no industrializados (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía).
    
  4. Gráfico del promedio de toneladas anuales de CO2 producidas por países desarrollados vs no desarrollados.
    
  5. Gráfico del promedio de toneladas anuales de CO2 por cemento producidas por países desarrollados vs no desarrollados.
    
  6. Gráfico del promedio de toneladas anuales de gas metano producidas por países desarrollados vs no desarrollados.
    
  7. Gráfico del promedio de toneladas anuales de óxido nitroso producidas por la industria en países desarrollados vs no desarrollados.
    
  8. Gráfico del promedio de toneladas anuales de CO2 por aceite producidas por países desarrollados vs no desarrollados.
    
  9. Gráfico del promedio de toneladas anuales de CO2 producidas por la industria en países desarrollados vs no desarrollados.
    
  10. Gráfico del promedio de consumo de energía por países desarrollados vs no desarrollados.
    
  11. Gráfico del promedio de toneladas anuales de CO2 producidas por carbón en países desarrollados vs no desarrollados.
    

# Funcionalidades extra

Creación de app para PC utilizando Flet en Python e integrando los gráficos de matplotlib.

 El directorio principal del código fuente es `src`, que incluye `main.py` como punto de entrada y `windowsControl.py` para el control de ventanas. Dentro de `src`, el subdirectorio `styles` contiene `colors.py` para definir los colores del proyecto. El directorio `components` alberga la lógica de los gráficos en `graficos.py`, datos en `owid-co2-data.csv`, y componentes en `molecules` y `atoms`, con archivos como `panels.py`, `windows.py`, `buttons.py` y `text.py`. Finalmente, el directorio `assets` contiene recursos gráficos como `banner.gif`, `icon.png`, `lg.png` y `loading.gif`. Esta estructura clara y organizada facilita el desarrollo y mantenimiento del proyecto.

# Estado del proyecto

El proyecto ha sido terminado.

# Agradecimientos

El equipo agradece a todos los participantes del equipo por su apoyo en la creación del mismo. Además, agradecemos cordialmente a nuestros profesores del programa de Samsung Innovation Campus por su enseñanza y acompañamiento en las clases y en el desarrollo de la investigación. Finalmente, agradecemos a todos aquellos que visiten y apoyen nuestro proyecto.
