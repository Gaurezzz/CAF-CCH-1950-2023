import pandas as pd
import datetime as dt
import seaborn as sns
import seaborn.objects as so
import plotly.graph_objects as go
import ipywidgets as widgets
from ipywidgets import interact

class Graficos:

    def __init__ (self):

        #IMPORTANDO EL DATAFRAME

        df = pd.read_csv("C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\components\\owid-co2-data.csv")

        df = df[df['iso_code'].str.contains('CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH', case=False, na=False)]

        fecha_inicio = 1950
        fecha_fin = 2023

        df = df[(df['year'] >= fecha_inicio) & (df['year'] <= fecha_fin)]

        #ELIMINANDO COLUMNAS

        columnas = [
            'gdp',
            'co2_growth_abs',
            'co2_including_luc', 'co2_including_luc_growth_abs',
            'co2_including_luc_growth_prct', 'co2_including_luc_per_capita',
            'co2_including_luc_per_gdp', 'co2_including_luc_per_unit_energy',
            'co2_per_gdp', 'consumption_co2_per_gdp', 'cumulative_cement_co2', 'cumulative_co2',
            'cumulative_co2_including_luc', 'cumulative_coal_co2',
            'cumulative_flaring_co2', 'cumulative_gas_co2', 'cumulative_luc_co2',
            'cumulative_oil_co2', 'cumulative_other_co2',
            'energy_per_gdp', 'flaring_co2', 'flaring_co2_per_capita', 'gas_co2',
            'gas_co2_per_capita', 'ghg_excluding_lucf_per_capita', 'ghg_per_capita',
            'land_use_change_co2', 'land_use_change_co2_per_capita',
            'share_global_cement_co2', 'share_global_co2',
            'share_global_co2_including_luc', 'share_global_coal_co2',
            'share_global_cumulative_cement_co2', 'share_global_cumulative_co2',
            'share_global_cumulative_co2_including_luc',
            'share_global_cumulative_coal_co2', 'share_global_cumulative_flaring_co2',
            'share_global_cumulative_gas_co2', 'share_global_cumulative_luc_co2',
            'share_global_cumulative_oil_co2', 'share_global_cumulative_other_co2',
            'share_global_flaring_co2', 'share_global_gas_co2',
            'share_global_luc_co2', 'share_global_oil_co2',
            'share_global_other_co2', 'share_of_temperature_change_from_ghg',
            'temperature_change_from_ch4', 'temperature_change_from_co2',
            'temperature_change_from_ghg', 'temperature_change_from_n2o',
            'total_ghg', 'total_ghg_excluding_lucf', 'trade_co2', 'trade_co2_share'
        ]


        df = df.drop(columns = columnas)

        #LIMPIANDO DATOS

        df = df.fillna(0)

        print(df.columns)

        import matplotlib.pyplot as plt

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        #CREANDO DATAFRAMES PER COUNTRY

        df_CHN = df[df['iso_code'].str.contains('CHN', case=False, na=False)]
        df_IND = df[df['iso_code'].str.contains('IND', case=False, na=False)]
        df_USA = df[df['iso_code'].str.contains('USA', case=False, na=False)]
        df_JPN = df[df['iso_code'].str.contains('JPN', case=False, na=False)]
        df_RUS = df[df['iso_code'].str.contains('RUS', case=False, na=False)]

        df_BRA = df[df['iso_code'].str.contains('BRA', case=False, na=False)]
        df_IDN = df[df['iso_code'].str.contains('IDN', case=False, na=False)]
        df_NGA = df[df['iso_code'].str.contains('NGA', case=False, na=False)]
        df_COD = df[df['iso_code'].str.contains('COD', case=False, na=False)]
        df_ETH = df[df['iso_code'].str.contains('ETH', case=False, na=False)]

        df_IND.set_index('year', inplace = True)

        #CREANDO EL PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_CHN['co2'], label='CHINA')
        ax_main.plot(df_IND.index, df_IND['co2'], label='INDIA')
        ax_main.plot(df_IND.index, df_USA['co2'], label='ESTADOS UNIDOS')
        ax_main.plot(df_IND.index, df_JPN['co2'], label='JAPÓN')
        ax_main.plot(df_IND.index, df_RUS['co2'], label='RUSIA')

        ax_main.plot(df_IND.index, df_BRA['co2'], label='BRAZIL')
        ax_main.plot(df_IND.index, df_IDN['co2'], label='INDONESIA')
        ax_main.plot(df_IND.index, df_NGA['co2'], label='NIGERIA')
        ax_main.plot(df_IND.index, df_COD['co2'], label='REPÚBLICA DEMOCRÁTICA DEL CONGO')
        ax_main.plot(df_IND.index, df_ETH['co2'], label='ETIOPÍA')

        ax_main.set_title('Toneladas de CO2 a lo largo del tiempo')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de CO2')

        plt.legend()

        self.g1 = main

        #PLOT INDUSTRIALIZADO

        main2, ax_main2 = plt.subplots(figsize=(12, 6))

        ax_main2.plot(df_IND.index, df_CHN['co2'], label='CHINA')
        ax_main2.plot(df_IND.index, df_IND['co2'], label='INDIA')
        ax_main2.plot(df_IND.index, df_USA['co2'], label='ESTADOS UNIDOS')
        ax_main2.plot(df_IND.index, df_JPN['co2'], label='JAPÓN')
        ax_main2.plot(df_IND.index, df_RUS['co2'], label='RUSIA')

        ax_main2.set_title('Toneladas de CO2 para países industrializados a lo largo del tiempo')
        ax_main2.set_xlabel('Año')
        ax_main2.set_ylabel('Toneladas de CO2')

        plt.legend()

        self.g2=main2


        #PLOT NO INDUSTRIALIZADO

        main3, ax_main3 = plt.subplots(figsize=(12, 6))

        ax_main3.plot(df_IND.index, df_BRA['co2'], label='BRAZIL')
        ax_main3.plot(df_IND.index, df_IDN['co2'], label='INDONESIA')
        ax_main3.plot(df_IND.index, df_NGA['co2'], label='NIGERIA')
        ax_main3.plot(df_IND.index, df_COD['co2'], label='REPÚBLICA DEMOCRÁTICA DEL CONGO')
        ax_main3.plot(df_IND.index, df_ETH['co2'], label='ETIOPÍA')

        ax_main3.set_title('Toneladas de CO2 para países NO industrializados a lo largo del tiempo')
        ax_main3.set_xlabel('Año')
        ax_main3.set_ylabel('Toneladas de CO2')

        plt.legend()

        self.g3 = main3

        #plt.show()

        #SACANDO DESARROLLADOS Y NO DESARROLLADOS

        df_desarrollado = df[df['iso_code'].str.contains('CHN|IND|USA|JPN|RUS', case=False, na=False)]
        df_no_desarrollado = df[df['iso_code'].str.contains('BRA|IDN|NGA|COD|ETH', case=False, na=False)]

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA EL CO2

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_co2_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['co2'])
        df_co2_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['co2'])

        #PONER BIEN LOS INDICES

        df_co2_desarrollado = df_co2_desarrollado.mean()
        df_co2_desarrollado = df_co2_desarrollado.reset_index()
        df_co2_desarrollado = df_co2_desarrollado.drop(columns = ['level_0'])
        df_co2_desarrollado.columns = ['year', 'mean_co2']

        df_co2_no_desarrollado = df_co2_no_desarrollado.mean()
        df_co2_no_desarrollado = df_co2_no_desarrollado.reset_index()
        df_co2_no_desarrollado = df_co2_no_desarrollado.drop(columns = ['level_0'])
        df_co2_no_desarrollado.columns = ['year', 'mean_co2']

        #PLOT

        main4, ax_main4 = plt.subplots(figsize=(12, 6))

        ax_main4.plot(df_IND.index, df_co2_desarrollado['mean_co2'], label='Países desarrollados')
        ax_main4.plot(df_IND.index, df_co2_no_desarrollado['mean_co2'], label='Países NO desarrollados')

        ax_main4.set_title('Promedio de toneladas anuales producidos por países desarrollados vs no desarrollados')
        ax_main4.set_xlabel('Año')
        ax_main4.set_ylabel('Toneladas de CO2 promedio')

        plt.legend()

        self.g4 = main4

        #plt.show()

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_cemento_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['cement_co2'])
        df_cemento_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['cement_co2'])

        #PONER BIEN LOS INDICES

        df_cemento_desarrollado = df_cemento_desarrollado.mean()
        df_cemento_desarrollado = df_cemento_desarrollado.reset_index()
        df_cemento_desarrollado = df_cemento_desarrollado.drop(columns = ['level_0'])
        df_cemento_desarrollado.columns = ['year', 'mean_cement_co2']

        df_cemento_no_desarrollado = df_cemento_no_desarrollado.mean()
        df_cemento_no_desarrollado = df_cemento_no_desarrollado.reset_index()
        df_cemento_no_desarrollado = df_cemento_no_desarrollado.drop(columns = ['level_0'])
        df_cemento_no_desarrollado.columns = ['year', 'mean_cement_co2']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_cemento_desarrollado['mean_cement_co2'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_cemento_no_desarrollado['mean_cement_co2'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de CO2 por cemento producidos por países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de CO2 por cemento promedio')

        plt.legend()

        self.g5 = main

        #plt.show()

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA METANO

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_methane_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['methane'])
        df_methane_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['methane'])

        #PONER BIEN LOS INDICES

        df_methane_desarrollado = df_methane_desarrollado.mean()
        df_methane_desarrollado = df_methane_desarrollado.reset_index()
        df_methane_desarrollado = df_methane_desarrollado.drop(columns = ['level_0'])
        df_methane_desarrollado.columns = ['year', 'mean_methane']
        df_methane_no_desarrollado = df_methane_no_desarrollado.mean()
        df_methane_no_desarrollado = df_methane_no_desarrollado.reset_index()
        df_methane_no_desarrollado = df_methane_no_desarrollado.drop(columns = ['level_0'])
        df_methane_no_desarrollado.columns = ['year', 'mean_methane']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_methane_desarrollado['mean_methane'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_methane_no_desarrollado['mean_methane'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de gas metano producidos por países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de gas metano promedio')

        plt.legend()

        self.g6 = main

        #plt.show()

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA OXIDO NITROSO

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_nitrous_oxide_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['nitrous_oxide'])
        df_nitrous_oxide_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['nitrous_oxide'])

        #PONER BIEN LOS INDICES

        df_nitrous_oxide_desarrollado = df_nitrous_oxide_desarrollado.mean()
        df_nitrous_oxide_desarrollado = df_nitrous_oxide_desarrollado.reset_index()
        df_nitrous_oxide_desarrollado = df_nitrous_oxide_desarrollado.drop(columns = ['level_0'])
        df_nitrous_oxide_desarrollado.columns = ['year', 'mean_nitrous_oxide']

        df_nitrous_oxide_no_desarrollado = df_nitrous_oxide_no_desarrollado.mean()
        df_nitrous_oxide_no_desarrollado = df_nitrous_oxide_no_desarrollado.reset_index()
        df_nitrous_oxide_no_desarrollado = df_nitrous_oxide_no_desarrollado.drop(columns = ['level_0'])
        df_nitrous_oxide_no_desarrollado.columns = ['year', 'mean_nitrous_oxide']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_nitrous_oxide_desarrollado['mean_nitrous_oxide'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_nitrous_oxide_no_desarrollado['mean_nitrous_oxide'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de oxido nitroso producidos por la industria en países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de oxido nitroso promedio')

        plt.legend()

        self.g7 = main

        #plt.show()

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA ACEITE

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_oil_co2_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['oil_co2'])
        df_oil_co2_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['oil_co2'])

        #PONER BIEN LOS INDICES

        df_oil_co2_desarrollado = df_oil_co2_desarrollado.mean()
        df_oil_co2_desarrollado = df_oil_co2_desarrollado.reset_index()
        df_oil_co2_desarrollado = df_oil_co2_desarrollado.drop(columns = ['level_0'])
        df_oil_co2_desarrollado.columns = ['year', 'mean_oil_co2']

        df_oil_co2_no_desarrollado = df_oil_co2_no_desarrollado.mean()
        df_oil_co2_no_desarrollado = df_oil_co2_no_desarrollado.reset_index()
        df_oil_co2_no_desarrollado = df_oil_co2_no_desarrollado.drop(columns = ['level_0'])
        df_oil_co2_no_desarrollado.columns = ['year', 'mean_oil_co2']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_oil_co2_desarrollado['mean_oil_co2'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_oil_co2_no_desarrollado['mean_oil_co2'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de CO2 por aceite producidos por países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de CO2 por aceite promedio')

        plt.legend()

        self.g8 = main

        #plt.show()


        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA OTROS

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_other_industry_co2_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['other_industry_co2'])
        df_other_industry_co2_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['other_industry_co2'])

        #PONER BIEN LOS INDICES

        df_other_industry_co2_desarrollado = df_other_industry_co2_desarrollado.mean()
        df_other_industry_co2_desarrollado = df_other_industry_co2_desarrollado.reset_index()
        df_other_industry_co2_desarrollado = df_other_industry_co2_desarrollado.drop(columns = ['level_0'])
        df_other_industry_co2_desarrollado.columns = ['year', 'mean_other_industry_co2']

        df_other_industry_co2_no_desarrollado = df_other_industry_co2_no_desarrollado.mean()
        df_other_industry_co2_no_desarrollado = df_other_industry_co2_no_desarrollado.reset_index()
        df_other_industry_co2_no_desarrollado = df_other_industry_co2_no_desarrollado.drop(columns = ['level_0'])
        df_other_industry_co2_no_desarrollado.columns = ['year', 'mean_other_industry_co2']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_other_industry_co2_desarrollado['mean_other_industry_co2'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_other_industry_co2_no_desarrollado['mean_other_industry_co2'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de CO2 producidos por la industria en países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de CO2 por aceite promedio')

        plt.legend()

        self.g9=main

        #plt.show()

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA EL GASTO DE ENERGIA

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_energy_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['primary_energy_consumption'])
        df_energy_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['primary_energy_consumption'])

        #PONER BIEN LOS INDICES

        df_energy_desarrollado = df_energy_desarrollado.mean()
        df_energy_desarrollado = df_energy_desarrollado.reset_index()
        df_energy_desarrollado = df_energy_desarrollado.drop(columns = ['level_0'])
        df_energy_desarrollado.columns = ['year', 'mean_energy_co2']

        df_energy_no_desarrollado = df_energy_no_desarrollado.mean()
        df_energy_no_desarrollado = df_energy_no_desarrollado.reset_index()
        df_energy_no_desarrollado = df_energy_no_desarrollado.drop(columns = ['level_0'])
        df_energy_no_desarrollado.columns = ['year', 'mean_energy_co2']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_energy_desarrollado['mean_energy_co2'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_energy_no_desarrollado['mean_energy_co2'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de consumo de energía por países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Energía')

        plt.legend()

        self.g10 = main

        #plt.show()

        #SACANDO EL PROMEDIO POR AÑO DESARROLLADO VS NO DESARROLLADO PARA CARBÓN

        #CHN|IND|USA|JPN|RUS|BRA|IDN|NGA|COD|ETH

        df_coal_co2_desarrollado = df_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['coal_co2'])
        df_coal_co2_no_desarrollado = df_no_desarrollado.pivot(index='iso_code', columns = ['year'], values = ['coal_co2'])

        #PONER BIEN LOS INDICES

        df_coal_co2_desarrollado = df_coal_co2_desarrollado.mean()
        df_coal_co2_desarrollado = df_coal_co2_desarrollado.reset_index()
        df_coal_co2_desarrollado = df_coal_co2_desarrollado.drop(columns = ['level_0'])
        df_coal_co2_desarrollado.columns = ['year', 'coal_co2']

        df_coal_co2_no_desarrollado = df_coal_co2_no_desarrollado.mean()
        df_coal_co2_no_desarrollado = df_coal_co2_no_desarrollado.reset_index()
        df_coal_co2_no_desarrollado = df_coal_co2_no_desarrollado.drop(columns = ['level_0'])
        df_coal_co2_no_desarrollado.columns = ['year', 'coal_co2']

        #PLOT

        main, ax_main = plt.subplots(figsize=(12, 6))

        ax_main.plot(df_IND.index, df_coal_co2_desarrollado['coal_co2'], label='Países desarrollados')
        ax_main.plot(df_IND.index, df_coal_co2_no_desarrollado['coal_co2'], label='Países NO desarrollados')

        ax_main.set_title('Promedio de toneladas anuales de CO2 producidos por carbón en países desarrollados vs no desarrollados')
        ax_main.set_xlabel('Año')
        ax_main.set_ylabel('Toneladas de CO2')

        plt.legend()

        self.g11 = main

        suma_co2 = df['co2'].sum()
        suma_cement_co2 = df['cement_co2'].sum()
        suma_coal_co2 = df['coal_co2'].sum()
        suma_oil_co2 = df['oil_co2'].sum()
        suma_methane = df['methane'].sum()
        suma_nitrous_oxide = df['nitrous_oxide'].sum()
        suma_other_industry_co2 = df['other_industry_co2'].sum()

        valores = [suma_cement_co2, suma_coal_co2, suma_oil_co2, suma_methane, suma_nitrous_oxide, suma_other_industry_co2]
        etiquetas = ['CO2 por Cemento', 'CO2 por Carbón', 'CO2 por Petróleo', 'Metano', 'Óxido Nitroso', 'Otros CO2 Industriales']

        plt.figure(figsize=(10, 6))
        plt.bar(etiquetas, valores, color='skyblue')

        plt.title('Suma de CO2 producido por los países analizados por Fuente desde 1950', fontsize=14)
        plt.xlabel('Categorías', fontsize=12)
        plt.ylabel('Valor CO2 (en toneladas)', fontsize=12)

        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()

        self.g12 = plt.gcf()

        df_industrializados_sumas = df[df['iso_code'].str.contains('CHN|IND|USA|JPN|RUS', case=False, na=False)]

        suma_co2_industrial = df_industrializados_sumas['co2'].sum()
        suma_cement_co2_industrial = df_industrializados_sumas['cement_co2'].sum()
        suma_coal_co2_industrial = df_industrializados_sumas['coal_co2'].sum()
        suma_oil_co2_industrial = df_industrializados_sumas['oil_co2'].sum()
        suma_methane_industrial = df_industrializados_sumas['methane'].sum()
        suma_nitrous_oxide_industrial = df_industrializados_sumas['nitrous_oxide'].sum()
        suma_other_industry_co2_industrial = df_industrializados_sumas['other_industry_co2'].sum()

        valores_industrial = [suma_cement_co2_industrial, suma_coal_co2_industrial, suma_oil_co2_industrial,
                            suma_methane_industrial, suma_nitrous_oxide_industrial, suma_other_industry_co2_industrial]
        etiquetas_industrial = ['CO2 por Cemento', 'CO2 por Carbón', 'CO2 por Petróleo', 'Metano', 'Óxido Nitroso', 'Otros CO2 Industriales']

        plt.figure(figsize=(10, 6))
        plt.bar(etiquetas_industrial, valores_industrial, color='coral')

        plt.title('Suma de CO2 producido por los países industrializados analizados por Fuente desde 1950', fontsize=14)
        plt.xlabel('Categorías', fontsize=12)
        plt.ylabel('Valor CO2 (en toneladas)', fontsize=12)

        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()

        self.g13 = plt.gcf()

        df_no_industrializados_sumas = df[df['iso_code'].str.contains('BRA|IDN|NGA|COD|ETH', case=False, na=False)]

        suma_co2_no_industrial = df_no_industrializados_sumas['co2'].sum()
        suma_cement_co2_no_industrial = df_no_industrializados_sumas['cement_co2'].sum()
        suma_coal_co2_no_industrial = df_no_industrializados_sumas['coal_co2'].sum()
        suma_oil_co2_no_industrial = df_no_industrializados_sumas['oil_co2'].sum()
        suma_methane_no_industrial = df_no_industrializados_sumas['methane'].sum()
        suma_nitrous_oxide_no_industrial = df_no_industrializados_sumas['nitrous_oxide'].sum()
        suma_other_industry_co2_no_industrial = df_no_industrializados_sumas['other_industry_co2'].sum()

        valores_no_industrial = [suma_cement_co2_no_industrial, suma_coal_co2_no_industrial, suma_oil_co2_no_industrial,
                            suma_methane_no_industrial, suma_nitrous_oxide_no_industrial, suma_other_industry_co2_no_industrial]
        etiquetas_no_industrial = ['CO2 por Cemento', 'CO2 por Carbón', 'CO2 por Petróleo', 'Metano', 'Óxido Nitroso', 'Otros CO2 Industriales']

        plt.figure(figsize=(10, 6))
        plt.bar(etiquetas_no_industrial, valores_no_industrial, color='plum')

        plt.title('Suma de CO2 producido por los países NO industrializados analizados por Fuente desde 1950', fontsize=14)
        plt.xlabel('Categorías', fontsize=12)
        plt.ylabel('Valor CO2 (en toneladas)', fontsize=12)

        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        
        self.g14 = plt.gcf()

        df_cola = df[df['iso_code'].str.contains('CHN|IND|USA|JPN|RUS', case=False, na=False)]
#BRA|IDN|NGA|COD|ETH

        def crear_grafico_pastel(year):

            df_filtrado = df_cola[df_cola['year'] == year]


            plt.figure(figsize=(16,12))
            plt.pie(df_filtrado['co2'], labels=df_filtrado['country'], autopct='%1.1f%%', startangle=90)
            plt.title(f'CO2 producido por países industrializados en {year}')
            plt.axis('equal')

        self.activate1 = interact(crear_grafico_pastel, year=widgets.IntSlider(min=df_cola['year'].min(), max=df_cola['year'].max(), step=1, value=df_cola['year'].min()))



#plt.show()
