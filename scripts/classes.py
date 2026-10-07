import requests
import pandas as pd

class Clima_Cidades:

    def __init__(self):
        pass

    def ler_dados(self, cidade):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
        res_geo = requests.get(url).json()
        return res_geo

    def gravar_dados(self, cidades):
        dados_cidades = []
        for cidade in cidades:
            info = self.ler_dados(cidade)

            if 'results' in info:
                resultado = info['results'][0]

                lat = resultado['latitude']
                lon = resultado['longitude']

                url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"
                resp_clima = requests.get(url_clima).json()["current"]

                dict_cidade = {
                "cidade": cidade,
                "data_hora": resp_clima["time"],
                "temperatura_celsius": resp_clima["temperature_2m"],
                "umidade_pct": resp_clima["relative_humidity_2m"]
            }
                
                dados_cidades.append(dict_cidade)

        df_capitais = pd.DataFrame(dados_cidades)

        return df_capitais
        