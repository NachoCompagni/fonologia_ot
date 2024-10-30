import pandas as pd
import os

# Ruta relativa al archivo Excel
excel_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'tabla.xlsx')

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(excel_path)

# Mostrar el DataFrame
print(df)

fonemas = ["i", "e", "ɛ", "ə", "a", "ɔ", "o", "u", "j", "w", "l", "ʎ", "ɾ", "r", 
           "m", "n", "ɲ", "ŋ", "p", "b", "β", "t", "d", "ð", "k", "g", "ɣ", "f", 
           "v", "s", "z", "ʃ", "ʒ"]

if len(fonemas) == len(df):
    df['name'] = fonemas
    print(df)
else:
    print("La lista 'fonemas' no coincide con el número de filas en el DataFrame.")
