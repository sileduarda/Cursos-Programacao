# Criando uma classe para limpeza de dados em Python 

import pandas as pd
import unicodedata

class LimpezaDados:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remover_valores_nulos(self):
        self.dataframe = self.dataframe.dropna()
        return self.dataframe

    def normalizar(self):
        def normalize(col):
            col = str(col).strip().upper().replace(" ", "_")
            col = unicodedata.normalize("NFKD", col).encode("ascii", "ignore").decode("utf-8")
            return col
        
        self.dataframe.columns = [normalize(col) for col in self.dataframe.columns]
        return self.dataframe

    
# Exemplo com um DF criado especificamente para teste
df = pd.read_csv(r"C:\Users\eduar\OneDrive\Documentos\Programacao\DIO\Python\Anotações e PDF's\exemplo_poo.csv", encoding="UTF-8", sep = ";")

#print(df.head())
df = LimpezaDados(df)


df.remover_valores_nulos()
# print(df.dataframe.head())

df.normalizar()
print(df.dataframe.head())