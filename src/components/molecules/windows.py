import flet as ft
from styles.colors import BACKGROUND_COLOR, INDUSTRY_COLOR, NINDUSTRY_COLOR, SECONDARY_COLOR, PRIMARY_COLOR
from components.atoms.text import h1, h2, h3, h4, p1, p2
from components.graficos import Graficos
from flet.matplotlib_chart import MatplotlibChart
from flet.plotly_chart import PlotlyChart


class Windows:

    def crearAnalisis(self):

        graficos = self.graficos

        contenido = ft.Column(

            controls = [
                h2("Analisis CAF-CCH 1950-2023"),
                h4("Factores que incrementan el aumento en el consumo de combustible y la huella de carbono y comparativa entre los 5 países industrializados con más contaminantes (China, India, Estados Unidos, Japón y Rusia) y los 5 países no industrializados con más contaminantes (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) entre 1950 y 2023."),
        
                p2("El aumento en el consumo de combustibles fósiles y las emisiones de CO₂ son factores clave en el cambio climático. Entre 1950 y 2023, los países industrializados (China, India, Estados Unidos, Japón y Rusia) han liderado las emisiones globales debido a su alto desarrollo industrial. Por otro lado, países no industrializados (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) enfrentan sus propios retos, como el crecimiento poblacional."),
                h4("Análisis de Toneladas de  CO2  a lo largo del tiempo en todos los paises bajo estudio"),
                MatplotlibChart(graficos.g1),
                p2("El gráfico muestra la evolución de las emisiones de CO₂ entre 1950 y 2023, revelando diferencias significativas entre países industrializados y no industrializados. China destaca como el mayor emisor global, con un crecimiento exponencial desde finales de los años 90 hasta superar las **12,000 toneladas** en 2023, impulsado por su rápida industrialización y dependencia del carbón. Por su parte, India presenta un aumento constante desde la década de 1990, alcanzando casi **3,000 toneladas** en los últimos años debido a su crecimiento económico y demográfico."),

                p2("Estados Unidos dominó las emisiones globales hasta mediados de los años 2000, con un pico cercano a **6,000 toneladas**, seguido de un ligero descenso, posiblemente relacionado con mejoras en eficiencia energética y la adopción de energías más limpias. Rusia y Japón muestran tendencias más estables, aunque con caídas significativas, especialmente en Rusia después de 1990, como resultado del cambio en su estructura económica tras la disolución de la Unión Soviética.  "),

                p2("En contraste, los países no industrializados tienen niveles de emisión considerablemente menores, aunque en aumento. Brasil e Indonesia destacan con un crecimiento moderado, vinculado principalmente a la deforestación y la quema de biomasa. Nigeria, la República Democrática del Congo y Etiopía mantienen cifras bajas a lo largo del periodo analizado, pero muestran un crecimiento leve en las últimas décadas."),

                h4("Análisis de Toneladas de  CO2  a lo largo del tiempo en paises industrializados"),
                MatplotlibChart(graficos.g2),
                p2("El gráfico muestra la evolución de las emisiones de CO₂ en países industrializados a lo largo del tiempo, reflejando un aumento significativo impulsado por el desarrollo económico y la industrialización. Si bien las emisiones crecieron de manera sostenida en la segunda mitad del siglo XX, a partir de los años 2000 se observa una aceleración marcada, especialmente en economías emergentes como China e India."),

                p2("Por otro lado, países como Estados Unidos y Rusia muestran una tendencia más estable en las últimas décadas, con ligeras reducciones debido a políticas ambientales, mejoras tecnológicas y cambios en la estructura económica. A pesar de estas diferencias, el gráfico evidencia que los países industrializados han sido históricamente los principales contribuyentes a las emisiones globales de CO₂, con un impacto acumulativo significativo en el cambio climático."),

                h4("Análisis de Toneladas de  CO2  a lo largo del tiempo en paises no industrializados"),
                MatplotlibChart(graficos.g3),

                p2("El gráfico muestra la evolución de las emisiones de CO₂ en países no industrializados a lo largo del tiempo. A diferencia de los países industrializados, las emisiones aquí son considerablemente más bajas, aunque muestran un aumento progresivo."),

                p2("Brasil e Indonesia lideran las emisiones entre estos países, con un crecimiento marcado desde finales del siglo XX debido a la deforestación y al uso de la biomasa como fuente de energía. Indonesia supera a Brasil en los últimos años, con picos superiores a 700 toneladas."),

                p2("Nigeria presenta un aumento gradual desde los años 70, asociado al crecimiento poblacional y la expansión de actividades agrícolas. En cambio, la República Democrática del Congo y Etiopía mantienen niveles muy bajos, con incrementos apenas perceptibles en las últimas décadas."),

                h4("Comparativa paises industrializados vs no industrializados"),

                MatplotlibChart(graficos.g4),

                p2("El gráfico muestra la diferencia en emisiones de CO2 entre países desarrollados y no desarrollados. Los países desarrollados tienen un crecimiento continuo y pronunciado en toneladas de CO2 promedio desde 1950 hasta 2023, mientras que los países no desarrollados mantienen niveles muy bajos con un crecimiento apenas perceptible."),

                MatplotlibChart(graficos.g5),

                p2("El gráfico muestra que las emisiones de CO2 por la producción de cemento en países desarrollados han crecido de manera constante desde 1950, con un aumento acelerado a partir de 1990 y picos alrededor de 2010 y 2020, reflejando una mayor actividad industrial y construcción. En contraste, los países no desarrollados presentan niveles de emisiones bajos y estables, con un incremento gradual pero mínimo. Esto evidencia una brecha significativa entre ambos grupos, donde los países desarrollados tienen un mayor impacto ambiental en términos de emisiones de CO2 relacionadas con la producción de cemento."),

                MatplotlibChart(graficos.g6),
                p2("El gráfico muestra la evolución del promedio de toneladas anuales de gas metano emitidas por países desarrollados y países no desarrollados en el periodo de 1950 a 2023. A lo largo del tiempo, se observa una tendencia ascendente en ambos casos, aunque con diferencias significativas en la magnitud de las emisiones, siendo los paises desarrollados los que mantienen un ritmo considerablemente más alto."),
                p2("En 1950, las emisiones de gas metano promedio en países desarrollados iniciaron alrededor de 300 toneladas anuales. A lo largo del tiempo, las emisiones aumentaron significativamente, superando las 800 toneladas anuales hacia el año 2023. Es importante detallar también estancamientos temporales entre 1990 y 2000, y luego un repunte importante a partir del año 2005."),

                p2("En 1950, las emisiones de gas metano promedio en paises no desarrollados inician en niveles considerablemente bajos, alrededor de 50 toneladas anuales. A diferencia de los países desarrollados, el crecimiento es más gradual, alcanzando valores cercanos a 300 toneladas anuales en el año 2023."),

                p2("Los niveles de metano presentados en la grafica pueden deberse principalmente al impacto de la industrialización, el transporte y las actividades económicas, los cuales dependen en gran medida de combustibles fósiles en el caso de los paises industrializados y a factores como la deforestación, la agricultura y la falta de tecnologías eficientes para el caso de los paises no desarrollados."),
                
                MatplotlibChart(graficos.g7),

                p2("El gráfico muestra la evolución del promedio de toneladas anuales de óxido nitroso (N₂O) emitidas por la industria en países desarrollados y países no desarrollados entre 1950 y 2023."),

                p2("En 1950, los países desarrollados iniciaron con un promedio cercano a 60 toneladas anuales. A partir de ahí, se observa un incremento constante y acelerado entre las décadas de 1960 y 1990, alcanzando su punto más alto (alrededor de 200 toneladas anuales) entre 2010 y 2023."),

                p2("Las emisiones de óxido nitroso en países no desarrollados son significativamente menores en comparación con los países desarrollados. En 1950, las emisiones rondaban las 20 toneladas anuales. A partir de 1970, las emisiones muestran un aumento constante, llegando a cerca de 80 toneladas anuales en 2023."),

                p2("En el gráfico se puede observar la gran brecha que existe en la emision de óxido nitroso entre los paises desarrollados y no desarrollados, sin embargo en los ultimos años se ha observado la estabilidad en los niveles de emision de este gas de efecto invernadero para el caso de los paises desarrollados, debido posiblemente a la implementación de políticas de mitigación y tecnologías alternativas. Opuestos al caso anterior, los paises no desarrollados presentan un aumento gradual de emisión de óxido nitroso, el cual podría estar relacionado a la industralizacion tardía y la falta de políticas ambientales estrictas."),

                MatplotlibChart(graficos.g8),
                p2("El gráfico muestra las emisiones de CO2 promedio por la producción de aceite entre países desarrollados y no desarrollados desde 1950. Las emisiones en países desarrollados han tenido un crecimiento significativo hasta alcanzar un pico cercano a las 1050 toneladas en la última década, con fluctuaciones a partir de los años 1980. Por otro lado, los países no desarrollados muestran un aumento mucho más gradual y constante, alcanzando valores apenas superiores a las 100 toneladas. Esta diferencia destaca una mayor producción y consumo de aceite en países desarrollados, resultando en un impacto ambiental considerablemente superior."),
                MatplotlibChart(graficos.g9),
                p2("El gráfico muestra una gran disparidad en las emisiones de CO₂ producidas por la industria en países desarrollados y no desarrollados entre los años 1950 y 2023. En los países desarrollados, se observa un crecimiento constante de las emisiones desde 1960, con un incremento pronunciado entre las décadas de 1980 y 2000, alcanzando un pico de aproximadamente 45 toneladas de CO₂ por unidad promedio a partir de 2010, donde luego se estabilizan. En contraste, las emisiones en los países no desarrollados permanecen prácticamente sin cambios a lo largo del tiempo, manteniéndose en niveles muy bajos comparados con los países desarrollados. Esto pone de manifiesto una marcada diferencia en la contribución industrial a las emisiones de CO₂ entre ambos grupos de países."),
                MatplotlibChart(graficos.g10),
                p2("La gráfica muestra la evolución del consumo promedio de energía entre países desarrollados y no desarrollados desde 1950 hasta 2022. Se observa que los países desarrollados tienen un consumo energético significativamente mayor, con una tendencia de crecimiento continuo y acelerado a lo largo de las décadas, especialmente a partir de 1960. En contraste, los países no desarrollados presentan un consumo mucho más bajo, con un aumento gradual pero marginal en comparación con los países desarrollados. Esta disparidad refleja una brecha energética considerable entre ambos grupos, probablemente debido a diferencias en industrialización, acceso a tecnologías y desarrollo económico."),
                MatplotlibChart(graficos.g11),
                p2("La gráfica muestra el promedio de toneladas anuales de CO₂ producidas por carbón en países desarrollados y no desarrollados desde 1950 hasta 2022. Los países desarrollados presentan un aumento constante y pronunciado en la emisión de CO₂ a lo largo del tiempo, con un crecimiento acelerado después del año 2000, alcanzando niveles significativamente altos. Por otro lado, los países no desarrollados muestran emisiones de CO₂ mucho más bajas, con un incremento muy leve a lo largo del período. La gran diferencia entre ambos grupos evidencia la relación entre desarrollo industrial, uso intensivo de combustibles fósiles y emisiones de carbono, destacando la mayor contribución de los países desarrollados al cambio climático."),
                h4("Otros análisis"),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\heat1.png"),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\heat2.png"),
                MatplotlibChart(graficos.g12),
                MatplotlibChart(graficos.g13),
                MatplotlibChart(graficos.g14),
                h4("Tendencias y predicciones"),
                h4("Tendencias de producción de CO2 para Estados Unidos"),
                p2("Aunque irregular, la tendencia para la producción de CO2 para Estados Unidos es hacia bajo, es decir, en promedio, cada año reducen la cantidad producida"),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\tend1.png"),
                h4("Tendencias de producción de CO2 para China"),
                p2("Históricamente, y basados en los últimos 10 años, laa tendencia para la producción de CO2 de China es hacia el alza, lo cual es muy preocupante."),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\tend2.png"),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\tend3.png"),
                ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\tend4.png"),
            ], 
            scroll=True
        )

        contenedor = ft.Container(content=contenido, expand=True, bgcolor=BACKGROUND_COLOR, padding=ft.padding.only(left = 10, right = 10, bottom = 50, top=50))

        return contenedor

    def crearInteractivos(): pass

    def crearConclusiones(self): 

        contenido = ft.Column(

            controls = [
                h2("Conclusiones"),

                p1("Entre 1950 y 2023, el análisis de las emisiones de CO₂ y otros gases de efecto invernadero evidencia profundas diferencias entre países desarrollados y no desarrollados, tanto en sus niveles de emisión como en los factores que las impulsan. Los países desarrollados, como China, India, Estados Unidos, Japón y Rusia, han liderado históricamente las emisiones globales debido a su intensa industrialización y elevado consumo energético. En estos países, las emisiones han mostrado un crecimiento acelerado a lo largo del tiempo, alcanzando picos significativos en las últimas décadas, resultado del desarrollo económico y la dependencia de combustibles fósiles."),

                p2("Por su parte, los países no desarrollados, como Brasil, Indonesia, Nigeria, la República Democrática del Congo y Etiopía, presentan niveles de emisión considerablemente más bajos. No obstante, han experimentado un aumento gradual, impulsado por factores como el crecimiento poblacional, la deforestación y la industrialización tardía. Aunque sus contribuciones absolutas al cambio climático son menores, las tendencias ascendentes sugieren la necesidad de adoptar medidas preventivas para evitar que sigan incrementándose."),

                p2("China se destaca como el principal emisor global, con un crecimiento exponencial desde finales de los años 90, impulsado por su rápida industrialización y la dependencia del carbón como fuente de energía. India, aunque a menor escala, ha mostrado un incremento constante, reflejo de su crecimiento económico y demográfico. Estados Unidos, que lideró las emisiones globales durante gran parte del siglo XX, ha experimentado una leve reducción en las últimas décadas, atribuida a mejoras tecnológicas y políticas ambientales. Japón y Rusia muestran tendencias más estables, aunque con variaciones notables relacionadas con cambios en sus economías y estructuras industriales."),

                p2("En los países no desarrollados, Brasil e Indonesia lideran las emisiones dentro de este grupo, principalmente debido a la deforestación y la quema de biomasa. Mientras tanto, Nigeria, Etiopía y la República Democrática del Congo mantienen niveles bajos de emisión, aunque con un incremento gradual en las últimas décadas."),

                p2("Finalmente, la comparación entre ambos grupos de países resalta una brecha significativa en sus impactos ambientales. Los países desarrollados no solo han contribuido más al cambio climático a lo largo del tiempo, sino que también enfrentan el reto de liderar las soluciones para mitigar estos efectos. Por otro lado, los países no desarrollados, aunque menos responsables históricamente, necesitan apoyo para implementar políticas sostenibles y tecnológicas que les permitan evitar repetir los errores de los países más industrializados.")
            ],
            scroll=True
        )

        contenedor = ft.Container(content=contenido, expand=True, bgcolor=BACKGROUND_COLOR, padding=ft.padding.only(left = 10, right = 10, bottom = 50, top=50))

        return contenedor
    
    def crearInicio(self): 

        contenido = ft.Column(

            controls = [

                h2("Bienvenido"),

                p2("El aumento en el consumo de combustibles fósiles y las emisiones de CO₂ son factores clave en el cambio climático. Entre 1950 y 2023, los países industrializados (China, India, Estados Unidos, Japón y Rusia) han liderado las emisiones globales debido a su alto desarrollo industrial. Por otro lado, países no industrializados (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) enfrentan sus propios retos, como el crecimiento poblacional."),
                p2('"Análisis de factores que incrementan el aumento en el consumo de combustible y la huella de carbono y comparativa entre los 5 países industrializados con más contaminantes (China, India, Estados Unidos, Japón y Rusia) y los 5 países no industrializados con más contaminantes (Brasil, Indonesia, Nigeria, República Democrática del Congo y Etiopía) entre 1950 y 2023" compara las emisiones y los patrones de contaminación entre ambos grupos, visualizando los datos históricos mediante gráficas generadas en Python para entender mejor las dinámicas y su impacto ambiental.'),

                ft.Container(
                    content = ft.Column(controls = [h4("Análisis"),
                        p2("En la página de análisis encontrarás gráficos y comparaciones sobre las emisiones de CO₂ y otros gases de efecto invernadero entre países industrializados y no industrializados desde 1950, destacando las principales fuentes de emisión y sus impactos en el cambio climático.")]), bgcolor=INDUSTRY_COLOR, margin=ft.margin.only(left=50, right=50, top=50, bottom=10), padding=50, ink=True,
                        on_click=lambda e: self.changeWindows(2)
                    ),

                ft.Container(
                    content = ft.Column(controls = [h4("Conclusiones"),
                        p2("Aqui Encontrarás un resumen de los hallazgos clave sobre las emisiones de CO₂, destacando las diferencias entre países desarrollados y no desarrollados, y la necesidad de adoptar políticas sostenibles para mitigar el impacto ambiental global.")]), bgcolor=NINDUSTRY_COLOR, margin=ft.margin.only(left=50, right=50, top=20, bottom=10), padding=50, ink=True,
                        on_click=lambda e: self.changeWindows(4)
                    ),

                ft.Container(
                    content = ft.Column(controls = [h4("Nuestro proyecto"),
                        p2('En "Nuestro proyecto" encontrarás información sobre los integrantes del equipo, un enlace al repositorio de GitHub donde puedes explorar el código y el desarrollo del proyecto, además de la bibliografía y las fuentes de datos clave que sustentan nuestro análisis y conclusiones.')]), bgcolor=SECONDARY_COLOR, margin=ft.margin.only(left=50, right=50, top=20, bottom=10), padding=50, ink=True,
                        on_click=lambda e: self.changeWindows(5)
                    ),
            ]
        )

        contenedor = ft.Container(content=contenido, expand=True, bgcolor=BACKGROUND_COLOR, padding=ft.padding.only(left = 10, right = 10, bottom = 50, top=50))

        contenedorTotal = ft.Container(content = ft.Column(
            controls = [ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\src\\assets\\banner.gif"),
            contenedor],
            scroll = True
        ))

        return contenedorTotal
    
    def crearNProyecto(self): 

        contenido = ft.Column(

            controls = [

                h2("Acerca de nuestro proyecto"),

                p1("Gracias por dedicar tiempo a explorar nuestro proyecto. 🌍 A lo largo de este trabajo, hemos analizado la evolución de las emisiones de CO₂ y otros gases de efecto invernadero, así como sus impactos en el cambio climático. 🌱 Esperamos que la información proporcionada te haya brindado una comprensión más profunda sobre las diferencias entre los países desarrollados y no desarrollados en cuanto a su contribución ambiental. 💡 Este análisis es solo un paso hacia una mayor conciencia y acción frente al cambio climático. 🌎 ¡Gracias por tu interés en este importante tema! 🌿"),

                h4("Integrantes"),
                p2('Sofia Lemus'),
                p2('Nelson Mejia'),
                p2('Gabriela Rodriguez'),
                h4("Link de GitHub"),
                p2("https://github.com/Gaurezzz/CAF-CCH-1950-2023"),
                h4("Dataset utilizado"),
                p2("https://ourworldindata.org/co2-and-greenhouse-gas-emissions#explore-data-on-co2-and-greenhouse-gas-emissions"),

                p2("Proyecto 1 realizado para Samsung Innovation Campus 2024"),
            ],
            scroll=True
        )

        contenedor = ft.Container(content=contenido, expand=True, bgcolor=BACKGROUND_COLOR, padding=ft.padding.only(left = 10, right = 10, bottom = 50, top=50))

        return contenedor

    def crearInteractivos(self):

        graficos = self.graficos

        contenido = ft.Column(

            controls = [
                h2("Graficos interactivos"),
                ft.Button("Haz click aqui para ver el grafico interactivo 1", on_click=lambda e: self.activate1)
            ], 
            scroll=True
        )

        contenedor = ft.Container(content=contenido, expand=True, bgcolor=BACKGROUND_COLOR, padding=ft.padding.only(left = 10, right = 10, bottom = 50, top=50))

        return contenedor



    def __init__ (self, changeWindows):

        self.graficos = Graficos()

        self.inicio = self.crearInicio()
        self.analisis = self.crearAnalisis()
        self.interactivos = self.crearInteractivos()
        self.conclusiones = self.crearConclusiones()
        self.proyecto = self.crearNProyecto()
        self.espera = ft.Container(bgcolor="#282828", content = ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\loading.gif"), padding=100)
        self.changeWindows = changeWindows
